from tkinter import *
import random

GAME_WIDTH = 800
GAME_HEIGHT = 700
SPEED = 70
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordiantes = []
        self.squares = [] # długość wężą - ilość kwadratów

        for i in range(0, BODY_PARTS):
            self.coordiantes.append([0, 0]) # snake pojawia się w lewym górnym rogu

        for x, y in self.coordiantes:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag= "snake")
            self.squares.append(square)

class Food:

    def __init__(self):
        # 700/50 = 14
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x,y]
        # tag dodajemy by później np. było łatwiej usunąć ten obiekt
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):

    x,y = snake.coordiantes[0]

    if direction == "up":
        y -= SPACE_SIZE # przesuwa się do daną odległość

    elif direction == "down":
        y += SPACE_SIZE # przesuwa się do daną odległość

    elif direction == "left":
        x -= SPACE_SIZE # przesuwa się do daną odległość

    elif direction == "right":
        x += SPACE_SIZE # przesuwa się do daną odległość

    snake.coordiantes.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score: {}".format(score))

        canvas.delete("food") # możemy tak usunąć dzięki tagowi który został wcześniej ustalony

        food = Food()

    else:
        del snake.coordiantes[-1] # usuwany jest koniec węża - by było że się porusza

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food) # to jest coś ale odświeżenie okna przed kolejnym ruchem

def change_directiopn(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x,y = snake.coordiantes[0]

    if x < 0 or x >= GAME_WIDTH:
        return True

    if y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordiantes[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True

def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('Arial',70), text="GAME OVER", fill="red", tag = "gameover")

window = Tk()
window.title("Snake Game :D")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text = "Score: {}".format(score), font = ('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2)) # dzieki tym zabiegom okno powinno się wyśrodkować do srodka naszego ekranu
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda  event: change_directiopn('left'))
window.bind('<Right>', lambda  event: change_directiopn('right'))
window.bind('<Up>', lambda  event: change_directiopn('up'))
window.bind('<Down>', lambda  event: change_directiopn('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()

