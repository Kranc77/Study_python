# plik poświęcony kursowi na YT
import time
# pętla while
'''
name = None  # ewentualnie dajemy ""

while not name:  # ewentualnie gdy warunek wyżej, to sporawdzamy długość len(name) == 0
    name = input("Podaj swoje imię: ")

print("Hello "+name)
'''
# pętla loop
# for "zmienna" in range("start","end","step")
'''
for i in range(10):
    print(i)
for i in range(50,100+1):
    print(i)
for i in "Bro Code":
    print(i)    # wypisanie każdej litery w podanej sekwencji
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print('Happy New Year!!!')

# nestled loops - pętla w pętli
rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #  end="" zapobiega przejściu do nowej linii
    print()  # nowa linia 
'''
# loop control statements
# break = zatrzymuje pętle
# continue = przechodzi do następnej iternacji w pętli
# pass = do nothing, acts as a placeholder / symbol zastępczy?
'''
while True:
    name = input("Enter your name: ")
    if name != "":
        break
        
phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="") # end="" zapobiega nowym liniom
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
'''
# list = used to store multiple items in a single variable
'''
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"
# print(food[0])
# food.append("ice cream")
# food.remove("hotdog")
# food.pop() # usuwa ostatni element
# food.insert(0, "cake")
# food.sort()
# food.clear() # usuwa wszystko


for x in food:
    print(x)
'''
# 2D list
'''
drinks = ["coffee", "soda", "beer"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[1][2])
'''
# tuple = collection which is ordered and unchangeable used to group together related data
'''
student = ("Bro", 21, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)
if "Bro" in student:
    print("Bro is here! ")
'''
# set - collection which is unordered, unindexed. No duplicate value
'''
utensils = {"fork", "spoon", "knife"} # set jest szybszy od list
# nie pozwala na duplikaty oraz nie ma indeksowania ( jak worek )
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) # mozna łączyc sety
dinner_table = utensils.union(dishes) # łączenie
for x in dinner_table:
    print(x)
print(utensils.difference(dishes)) # co ma utensils a nie ma dishes
print(utensils.intersection(dishes)) # to co mają wspólne
'''
# dictionary = A changeable, unordered colection of unique key: value pairs
# Fast because they use hashing, allow us to access a value quickly
'''
capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China') # usunięcie danej wartości
capitals.clear() # wyczyszczenie słownika

# print(capitals.get('Germany')) # sprawdzanie czy dana wartośc się znajduje w słowniku
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items()) # wypisanie par

for key, value in capitals.items():
    print(key, value)
'''
'''
# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "bro Code!"

if(name[0].islower()):
    name = name.capitalize() # capitalize zmienia pierwszą literę na dużą
first_name = name[:3].upper() # gdy zaczynamy od początku to nie potrzebujemy podawać 0 na początku
last_name = name[4:].lower() # gdy nie podam jak długie jest nazwisko tylko zostawie miejsce to oznacza że do końca
last_character = name[-1]
print(first_name)
print(last_name)
print(last_character)
'''
# function = a block of code which is executed only when it is called
'''
def hello(first_name, last_name,age):
    print("Hello " + first_name + " " + last_name)
    print("You are "+ str(age) + " years old.")
    print("Have a nice day! ")

# hello("Bro", "Code", 21)
# liczba parametrów musi się zgadzać ! 
'''
# return statment = Function send Python values/objects bact to the caller.
#                   These values/objects are know as the function's return value
'''
def multiply(n1, n2):
    return n1 * n2

x = multiply(6,2)
print(x)
'''
# keywords arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments thet uor function receives
'''
def hello(first, middle, last):
    print("Hello "+first+" "+ middle+" "+last)

hello(last="Code",middle="Dude",first="Bro")
# chodzi po porstu o kolejność jeśli jest wpisywana inaczej 
'''
# nested functions calls = function calls inside other function calls innermost function calls are resolved first
#                         returned value is used as argument for the next outher function
'''
print(round(abs(float((input("Enter a whole positive number: "))))))
# nested functions calls - funkcje zagnieżdżone - nie są rozbijane
'''
# scope = The region that a variable is recognized
#           A variable is only avilable form inside the region it is created
#           A global and locally scoped versions of variable can be created
name = "Andrzej "   # global scope (available inside & outside functions # zmienna globalna
'''
# global scope - zasięg globalny
def display_name():
    name = "Code"   # local scope ( available only inside this functon ) # zmienna lokalna xD
    print(name)
display_name()
print(name)
'''
# *args =   parameter that will pack all arguments into a tuple useful so that a function can accept
#           a varying amount of arguments
#  podajemy po prostu listę argumentów a w funkcji to uwzględniamy
# trzeba pamiętać że podajemy tuple (krotkę) więc chcąc na niej działać trzeba ją zamienić na liste
'''
def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0]=0
    for i in stuff:
        sum += i
    return sum
print(add(1,2,3,4,5,6))
'''
# **kwargs =    parameter that will pack all arguments into a dictionary
#               useful so that a function can accept a varying amount of keyword arguments
#  czyli podajemy słownik zamiast tuple
'''
def hello(**kwargs): # pamiętać że muszą być te dwie gwiazdki bo potem nazwa może być różna 
    # print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello" , end=" ")
    for key, value in kwargs.items():
        print( value, end= " ")
hello(title = "Mr.", first="Bro",middle = "Dude", last="Code")
'''
# str.format() =    optional method that gives users more control when displaying output
# sposób zapisania inaczej printa - bardziej estetyczny
'''
# animal = "cow"
# item = "moon"
# print("The "+animal+" jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {1}".format(animal, item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="mood")) # keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal,item))
# name = "Bro"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name)) # {:10} to oznacza 10 spacji po
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) # {:10} to oznacza 10 spacji po
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) # {:10} to oznacza 10 spacji przed
# print("Hello, my name is {:^10}. Nice to meet you".format(name)) # {:10} to oznacza 10 spacji a napis wyśrodkowany
number = 1000
print("The number pi is {:.3f}".format(number)) # zaokrągla do 3 miejsc po przecinku
print("The number pi is {:,}".format(number))   # dzieli na tysiące
print("The number pi is {:b}".format(number))   # zamiana na binarny
print("The number pi is {:o}".format(number))   # zamiana na ósemkowy
print("The number pi is {:X}".format(number))   # zamiana na szestnastkowy
print("The number pi is {:E}".format(number))   # format matematyczny 
'''
# liczby pseudo-randomowe
'''
import random

x = random.randint(1,6)
y = random.random()
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) # losowanko z papier kamień nożyce

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards) # losowe przelosowanie xD
print(cards) # karty po przelosowaniu
'''
# exception = events detected during execution that interrupt the flow of a program
# wyjątki...
'''
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! Idiot! ")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(result)
finally: # to zawsze się wykonuje 
    print("This will always execute")
'''
# file detection - sprawdzenie czy plik istnieje
'''
import os

path  = "C:\\Users\\andrz\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exists!")
'''
# reading a file - czytanie pliku
'''
try:
    with open('C:\\Users\\andrz\\Desktop\\test.txt') as file:
        print(file.read())
except:
    print("That file was not found :(")
# print(file.close()) # sprawdzenie czy plik został zamknięty
'''
# Zapisywanie do pliku
'''
# text = "Yooooooo\nThis is some text\nHave a good one!"
text = "This text was overwritten"

with open('C:\\Users\\andrz\\Desktop\\test.txt','w') as file: # otwieramy w trybie do zapisu 'w'
    file.write(text) # pamiętać że plik jest nadpisywany
'''
# copy file() = copies contents of a file
# copy() =      copyfile() + permission mode + destiantion can be a directiory
# copy2() =     copy() + copies metadata (file's creation and modification times)
# kopiowanie plików
'''
import shutil

shutil.copyfile('C:\\Users\\andrz\\Desktop\\test.txt','copy.txt')
'''
# moving files
# by to działało to musi być  to robione na jednym dysku
'''
import os
source = "copy.txt"
destination = "D:\\Do_nauki\\copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
'''
# delete files - usuwanie plików i folderow
'''
import os
import shutil

path = "test.txt"
# os.remove(path) # usuwa plik
try:
    # os.remove(path)     # delete a file
    # os.rmdir(path)      # delete an empty directory
    # shutil.rmtree(path) # delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have premission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
'''
# module = a file containing python code. May contain functions, classes, etc
# Used with modular programming, which is to separate a program into parts
# można też dać from messages import *      ale może to w większych programach spowodować kolizje nazw
'''
# import messages as msg
from messages import hello, bye
# msg.hello()
# msg.bye()
hello()
bye()
help("modules")
# Jest też strona z bibliotekami standardowymi chyba "Python Module Index"
'''
#  gra papier kamień nożyce
'''
import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None
    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower() # zamieniamy na małe

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")
    play_again = input("Play again? (yes/no): ").lower()
    if play_again !="yes":
        break
print("Bye!")
'''
# quiz game
# gra na A, B, C, D
# -------------------------
'''
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)
# -------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# -------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("RESULT")
    print("----------------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+ str(score)+"%")
# -------------------------
def play_again():

    response = input("Do you want to play again? (yes/no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------
questions = {
    "Who crated Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"}
# pytania zostały tu zrobione za pomocą słownika
options = [["A. Guido van Rossum", "B. Elon Musk", "C BIll Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D.SNL"],
           ["A. True", "B. False", "C. Sometimes xD ", "D. What's Earth?"]]
# Do opcji została wykorzystana lista w liście

new_game()
# pętla do nowych gier
while play_again():
    new_game()
print("------------------------------\nBYE!!!!")
'''
# -------------------------------------------------------
# PYTHON OBJECT ORIENT PROGRAMMING (POOP)

# PATRZ PLIK car.py
'''
from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford", "Mustang",2022, "red")
# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

car_1.drive()
car_2 .stop()
'''

# differences between class and instant variables
'''
from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford", "Mustang",2022, "red")
car_1.wheels = 2    # jeśli np. to motocykl
# print(car_1.wheels)
# print(car_2.wheels)
# print(Car.wheels)
Car.wheels = 2      # można zmieniać stałą wartość dla wszystkich obiektów klasy w głównym programie i będzie to działać
print(car_1.wheels)
print(car_2.wheels)
'''

# inheritance in python
# czyli chodzi o dziedziczenie
'''
class Animal:
    alive = True    # class variable

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

# by stworzyć klasę która ma klasę-matkę to w nawiasie podajemy klasę z której dziedziczymy
class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")
class Fish(Animal):
    def swim(self):
        print("This fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.run()
fish.swim()
hawk.fly()
'''

# multi-level inheritance = when a derived (child) class inherits another derived (child) class
# dziedziczenie pochodne - dziedziczenie z klasy która także coś dziedziczy już
# to jest podobne do drzewa rodzinnego (family tree)
'''
class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")
class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog = Dog()

print(dog.alive)
dog.eat()
dog.bark()
'''

# multiple inheritance = when a child class is derived from more than one parent class
# dziedziczenie po więcej niż jednym rodzicu
'''
class Prey: # prey to ofiara
    def flee(self): # flee to uciekać
        print("This animal flees")

class Predator: # Predator - drapieżnik
    def hunt(self): # hunt - polować
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()
fish.flee()
fish.hunt()
'''
# method overriding in python
# chodzi o nadpisywanie
'''
class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):

    def eat(self):
        print("This rabbit is eating a carrot")
# no i ogólnie tak wygląda nadpisanie - czyli ta sama nazwa w klasie która już coś dziedziczy
rabbit = Rabbit()
rabbit.eat()
'''
# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and return self
# wywołanie wielu metod na tym samym obiekcie sekwencyjnie?
'''
class Car:
    def turn_on(self):
        print("You start the engine")
        return self
    def drive(self):
        print("You drive the car")
        return self
    def brake(self):
        print("You step on the brakes")
        return self
    def turn_off(self):
        print("You turn off the engine")
        return self
car = Car()

# car.turn_on().drive()

# car.brake().turn_off()
# ten "\" oznacza kontynuowanie komendy w nowej linii
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
# ten methon chaining polega na tym że można dane funcje z klasy wywoływać zaraz po sobie
# trzeba tylko pamiętać by zwrócić w klasie "self" w każdej funkcji
'''
# super() = Function used to give access to the methods of the parent class.
#           Returns a temporary object of a parent class when used
# służy do dostania się do klasy nadrzędnej
# chodzi o wykorzystnie funkcji klasy nadrzędnej wraz z jej parametrami jeśli mają coś wspólnego
'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length,width)
    def area(self):
        return self.width * self.length
class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.width * self.length * self.height
square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())
'''
# !!! całkiem ważne
# Prevents a user from crating an object of that class # coś ala ghost class - szablon
# + compels a user to override abstract methods in a child class

# abstract class =  a class which contains one more abstract methods
# abstract method = a method that has a declaration but does not have an implementation.
# abstract class ma zapobiec możliwości stworzenia przez użytkownika obiektu tej klasy
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("This car is stopped")
class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("This motorcycle is stopped")
# vehicle = Vehicle() - abstract ma zapobiec możliwości stworzenia obiektu tej klasy - wyrzuci błąd po prostu
car = Car()
motorcycle = Motorcycle()

# vehicle.go() - nie można korzystać z abstrakcyjnych funkcji/ metod
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()
# ogólnie rzecz mówiąc to abstract class i abstract method są jakby szablonem który trzeba nadpisać by program działał
# Car jest pojazdem typu Vehicle i musi mieć nadpisane takie metody jak "go" czy "stop" bo takie są w szablonie
# bo każdy pojazd dziedziczony po Vehicle powinien mieć takie metody - zapobiega to wkradaniu się błędów i programista
# też będzie pamiętał by to nadpisać bo inaczej będzie wyrzucało błąd
'''
# pass objects as arguments
# przekazywanie obiektów jako argumenty
# gdy podajemy parametry to muszą one się zgadzać w funkcji którą piszemy - piszemy funkcję zmieniającą paramtery klasy
# którą chcemy przekazać to musimy pamiętać by w funckji paramter tej klasy się zgadzał z stanem faktycznym
'''
class Car:

    color = None
class Motorcycle:

    color = None
def change_color(car, color):

    car.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
'''
# Duck typing = concept where the class of an object is less important than methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck, and it quacks like a duck, then it must be a duck."
'''
class Duck:

    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken:

    def walk(self):
        print("This chiken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You cauth the critter")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
# w skrócie to funkcja catch zadziała gdy klasa "duck" W NIEJ OPISANA będzie posiadała dane metody wktóre są wymagane
# chodzi o "walk" i "talk" wtedy np. kurczak może być uznany za "kaczkę" chodź nią nie jest, jakby np. nie chodził to 
# zwróci nam ta funckja error gdyż nie będzie klasa "chiken" nie będzie miała atrybutu "walk" i nie będzie
# wtedy kurczakiem
'''
# walrus operator :=        # operator morsa?

# net to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression
'''
# happy = True
# print(happy)

# print(happy = True)   # to zwróci błąd
# print(happy := True)    # tak będzie to działało oraz dana zmienna zostanie utworzona

# prosty program :
# foods = list()
# while True:
#     food = input("What food do you like: ")
#     if food == "quit":
#         break
#     foods.append(food)
# ----------------------------------
# teraz drugi sposób za pomocą operatora ":=" (czyli tego walrus operator) - będzie mniej linii kodu

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
'''
# assign function to a variable
# przypisanie funkcji do zmiennej
'''
def hello():
    print("Hello")

# print(hello) # coś takiego spowoduje wyświetlenie adresu funckji w pamięci komputera
# hi = hello  # przypisanie adresu funkcji (bez nawiasów "()") do zmiennej
# print(hi)   # wyświetlenie zawartości zmiennej (czyli adresu funckji hello)
# hello()
# hi()        # coś takiego spowoduje wykonanie funkcji hello() ale pod inną nazwą (coś ala alias)

say = print
say("Whoa!! I can't believe this works! :o")
# czyli stworzyliśmy coś ala kopię funckji print ale pod inną nazwą i możemy wykonywać teraz daną funckję
# ale pod różnymi nazwami jakimi chcemy
'''

# Higher Order Functions =  a function that either:
#                           1. accepts a function as an argument
#                           or
#                           2. returns a function
#                           (In python, functions are also treated as objects)
# czyli funkcja która przyjmuje jako argument funkcję albo zwraca funkcję
'''
# def loud(text):
#     return text.upper()
#
# def quiet(text):
#     return text.lower()
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
# hello(loud)
# hello(quiet())

def divisor(x):
    def divident(y):
        return y/x
    return divident
divide = divisor(2)
print(divide(10))
print(divide) # do zmiennej divide przypisaliśmy adres funkcji
# chodzi o to że najpierw wowołujemy zewnętrzną funkcję (divisor) która zwraca nam funkcję którą ma wewnątrz, a tą
# z kolei wywołujemy dodając nawias i wpisując liczbę bo inaczej ona sama by była zmienną
'''
# lambda function = function written in 1 line using lambda keyword accepts any number of arguments, but only has
#                   one expression. (think of it as a shortcut) (useful if needed a short period of time, throw-away)
#   W skrócie to jakoś funckja z dowolną ilością argumentów, jednym wyrażeniem, gdy jest potrzebna na chwilę
# lambda parameters:expression
'''
# normalny sposób:
# def double(x):
#     return x * 2
# print(double(5))
# za pomocą lambdy:
double = lambda x:x * 2
print(double(5))
multiply = lambda x, y: x * y
print(multiply(5,6))
add = lambda x, y, z: x + y + z
print(add(1,2,3))
full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Bro","Code"))
age_check = lambda age: True if age >=18 else False
print(age_check(29)) # czyli to są takie skróty
'''
# sort() method =   used with lists
# sort() function = used with iterables
'''
# students = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")
# students.sort(reverse=True) # reverse = True oznacza w odwrotnej kolejności i to działa na listy
# sorted_students = sorted(students, reverse=True)
# for i in students:
#     print(i)
# for i in sorted_students:
#     print(i)
students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)
            ]
grade = lambda grades:grades[1] # to spowoduje wybranie drugiej kolumny - jest to skrót funkcji w której to dostajemy
# się do drugiej kolumny
age  = lambda ages:ages[2]
students.sort(key=age)
# jeśli zamiast listy mielibyśmy tuple to wykorzystalibyśmy :
# sorted_students = sorted(students,key=age)
for i in students:
    print(i)
'''
# map() =   applies a function to each item i na iterable (list, tuple, etc)
#
# map(function, iterable)
# mapuje - zmienia wartości każdej iteracji w danej liście/tupli itp za pomocą podanej funkcji
'''
store = [("shirt", 20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]
to_euros = lambda data: (data[0],data[1]*0.82)
to_dollars = lambda data: (data[0], data[1]/0.82)

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)
'''
# filter() =    create a collection of elements from an iterable for which a function returns true
# filtruje dane
# filter(function, iterable)
'''
friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18
drinking_boddies = list(filter(age,friends))

for i in drinking_boddies:
    print(i)
'''
# reduce() =    apply a function to an iterable and reduce it to a single cumulative value.
#               performs function on first two elements and repeats process until 1 value remains
# tak jakby zmniejsza ilość elementów - z kilku łączy w jeden (literki w słowa itp)
# reduce(function, iterable)
'''
import functools
# letters = ["H","E","L","L","O"]
# word = functools.reduce(lambda x, y: x + y,letters)
# print(word)
factorial = [5,4,3,2,1]
result = functools.reduce(lambda x, y: x * y,factorial) # coś ala silnia # będzie to wymnażać wartości w liście 
print(result)
'''
# list comprehension =  a way to create a new list with less syntax can mimic certain lambda functions, easier to read
#                       lista z mniejszą ilością składni?
# 1                     lista = [expression for item in iterable]
# 2                     lista = [expression for item in iterable if conditional]
# 3                     lista = [expression if/else for item in iterable]
'''
# squares = []                # create an empty list
# for i in range(1,11):       # create a for loop
#     squares.append((i*i))   # define what each loop iteration should do
# print(squares)
# teraz za pomocą list comprehension # 1
# squares = [i * i for i in range(1,11)]
# print(squares)
# --------------------------------------------------------------------------------------------------
students = [100,90,80,70,60,50,40,30,0]
passed_students = list(filter(lambda  x: x >=60, students))
print(passed_students)
# teraz za pomocą list comprehension # 2
passed_students = [i for i in students if i >= 60]
print(passed_students)
# teraz za pomocą list comprehension # 3
passed_students_v2 = [i if i >= 60 else "FAILED" for i in students]
print(passed_students_v2)
'''
# dictionary comprehension = create dictionaries using an expression can replace for loops and certain lambda functions
#                           tworzenie słowników za pomocą wyrażenia może zastąpić pętle lub funkcje lambda
# 1 # dictionary = {key: expression for (key,value) in iterable}
# 2 # dictionary = {key: expression for (key,value) in iterable if conditional}
# 3 # dictionary = {key: (if/else) for (key,value) in iterable}
# 4 # dictionary = {key: function(value) for (key,value) in iterable}
# zamiana Farenhaita na Celcius za pmocą metody # 1
'''
# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
# print(cities_in_C)
# -------------------------------------------------------------------------------------------------------
# za pomocą metody # 2
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather)
# -------------------------------------------------------------------------------------------------------
# za pomocą metody # 3
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value>=40 else "COLD") for (key, value) in cities.items()}
# print(desc_cities)
# -------------------------------------------------------------------------------------------------------
# za pomocą metody # 4 - za pomocą osobnej funkcji
def check_temp(value):
    if value >= 70:
        return "HOT"
    elif 69 >= value >= 40:
        return "WARM"
    else:
        return "COLD"
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
desc_cities = {key: check_temp(value) for (key, value) in cities.items()}

print(desc_cities)
'''
# zip(*iterables) = aggregate from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each  element
# połączenie kilku obiektów iteracyjnych w jeden
'''
usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021","1/2/2021","1/3/2021"]
# users = list(zip(usernames, passwords)) # zamiana typu "zip" na "list"
# users_v2 = dict(zip(usernames, passwords)) # zamiana typu "zip" na "słownik"
# print(type(users))
# for i in users:
#     print(i)
# for key,value in users_v2.values():
#     print
users = zip(usernames, passwords, login_date)
for i in users:
    print(i)
'''
# *********************************************************************
# if __name__ == '__main__'
# *********************************************************************

# y tho? -  why throught? - Dlaczego jednak?
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is __name__
# then Python will execute the code found within __main__
'''
if __name__ == '__main__':
    pass
else:
    print("plik uruchomiony z importu")
# chodzi o to chyba by sprawdzić czy moduł(program jest odpalany samodzielnie) - jeśli w innym programie importowaliśmy
# ten moduł to nie wykona się instrukcja z "if __name__ == '__main__': " tylko z "else: " bo to nie bedzie moduł już
# uruchamiany bezpośrednio (czyli __main__) tylko __name__ przyjmie nazwę modułu zamiast "__main__"
'''
# ---------------------------------------------------------------------------
# czas
# ---------------------------------------------------------------------------
'''
import time

# print(time.ctime(0)) # czas epic - od którego komputer myśli że czas się rozpoczął (punkt odniesienia)?
                    # convert a time expressed in seconds snce epoch to a readable string
                    # epoch = when your computer thinks time began (reference point)

# print(time.time())  # return current seconds since epoch
# print(time.ctime(time.time()))  # aktualny czas

# time_object = time.localtime() # pełny czas lokalny
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object) # skrócona wersja czasu lokalnego
# print(local_time)
# time_object = time.gmtime() # UTC time
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y") # zamiana na "pełny" czas
# print(time_object)
time_tuple = (2020, 4, 20, 4, 30, 5, 0, 0, 0)
time_string = time.asctime(time_tuple) # tuple representation to normal string
time_string_seconds = time.mktime(time_tuple) # zamiana tuple na czas ale podany w sekundach (from epoch)
print(time_string_seconds)
'''
# thread =  a flow of execution. Like a separate order of instructions.
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock),
#           allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound =   program/task spends most of it's time waiting for internal events (CPU intensive) use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#               use multithreading
'''
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")
def drink_coffee():
    time.sleep(4)
    print("You drank coffee")
def study():
    time.sleep(5)
    print("You finish studying")

# eat_breakfast() # to się wykonuje sekwencyjnie więc wszystko wykona się po 12 sekundach dopiero
# drink_coffee()
# study()

# MULTITHREADING
# teraz uruchamiamy i używamy 4 wątków zamiast 1 więc wszystko wykona się już po 5 sekundach
x = threading.Thread(target=eat_breakfast, args=())
x.start()
y = threading.Thread(target=drink_coffee, args=())
y.start()
z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count()) # ilość aktywnych wątków
print(threading.enumerate())    # numer wątku/wątków
print(time.perf_counter())      # czas pracy?
'''

# daemon thread =   a thread that runs in the background, not important fro program to run ou program will not wait for
#                   daemon threads to complete before exiting non-deamon threads cannot normally be killed, stay alive
#                   until task is complete
#
#                   ex. background tasks, garbage collection, waiting for input, long running processes
# jest on do czasu dopuki jakieś zadanie nie zostanie wykonane
'''
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ",count," seconds")

x = threading.Thread(target=timer, daemon= True)
x.start()
# x.setDaemon(True) # to ustawienie nie działą
# print(x.isDaemon()) # nie działa z jakiegoś powodu
answer = input("Do you wish to exit?\n")
'''

# Python multiprocessing

# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for thread
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)
'''
from multiprocessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

# w zależności od ilości rdzeni możemy podzielić zadanie na poszczególne rdzenie przez co skróci się czas wykonania
# zadania. Poniżej jest przedstawione liczenie do miliona za pomocą 4 rdzeni (do 6 rdzeni można), większa ilość
# przypisanych rdzeni niż mamy spowolni działanie zamiast maksymalnie przyśpieszyć 
def main():

    print(cpu_count()) # sprawdzenie ile się ma dostępnych rdzeni

    a = Process(target=counter, args=(250000000,))
    a.start()

    b = Process(target=counter, args=(250000000,))
    b.start()

    c = Process(target=counter, args=(250000000,))
    c.start()

    d = Process(target=counter, args=(250000000,))
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()

    print("finished in: ",time.perf_counter()," seconds")


if __name__ == '__main__':
    main()
'''
# tworzenie graficznego interfejsu użytkownika :D
# graphical user interface (GUI)
'''
from tkinter import *
from PIL import ImageTk, Image
# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()   # instantiate an instance of a window # utworzy instancję okna
window.geometry("420x420") # zmiana rozmaru okna
window.title("Moje pierwsze GUI program")

icon = ImageTk.PhotoImage(Image.open("logo.png")) # zmiana loga(sposób z filmiku nie działał ale znalazłem ten i działa)
window.iconphoto(True, icon)
window.config(background="black")   # zmiana koloru tła

window.mainloop() # place window on computer screen, listen for events
'''
# label = an area widget that holds text and/or an image within a window
from tkinter import *
from PIL import ImageTk, Image
'''
window = Tk()
photo = ImageTk.PhotoImage(Image.open("logo.png"))
label = Label(window, text="Hello world",
              font=('Arial',40,'bold'),
              fg='#00FF00',
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20, # odstępy na osi x
              pady=20, # odstępy na osi y
              image=photo, # dodanie zdjęcia
              compound='bottom' # ustawienie zdjęcia
              )  # stworzenie label
label.pack() # dodanie label do okna
# label.place(x=0,y=0) # dodanie label w konkretnym miejscu okna

window.mainloop()   # wyświetlenie na ekranie okna
'''
# ------------------------------------------------
# button = you click it, then it does stuff
# ------------------------------------------------
'''
count = 0
def click():
    global count
    count += 1
    print(count)
window = Tk()
photo = ImageTk.PhotoImage(Image.open("like_button.jpg"))
button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()
'''
# ------------------------------------------------
# entry widget =    textbox that accepts a single line of user input
# ------------------------------------------------
'''
def submit():
    username = entry.get()
    print("Hello "+username)
    entry.config(state=DISABLED)    # spowoduje to zablokowanie dalszej możliwości edytowania tekstu
def delete():
    entry.delete(0,END) # usuwa tekst zapisany przez nas
def backspace():
    entry.delete(len(entry.get())-1,END)
window = Tk()

entry = Entry(window,
              font=("Arial",50),
              fg="#00FF00",
              bg="black",
              show="*") # show="*" spowoduje że każda litera wpisywana będzie schowana pod tym właśnie znakiem
entry.insert(0,'Spongebob') # tak jakby tekst podstawowy
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
'''
# ------------------------------------------------
# check box
# ------------------------------------------------
'''
def display():
    if(x.get()==1): # przy zasatosowaniu True/False nie trzeba porównywać tego do 1
        print("You agree!")
    else:
        print("You don't agree :(")

window = Tk()

x = IntVar()
photo = ImageTk.PhotoImage(Image.open("like_button.jpg"))
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=1,   # albo True
                           offvalue=0,  # albo False
                           command=display,
                           font=('Arial',20),
                           fg='#00FF00',
                           bg='black',
                           activeforeground='#00FF00',
                           activebackground='black',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')
check_button.pack()

window.mainloop()
'''
# ------------------------------------------------
# radio button - similar to checkbox, but you can only select one from a group
# ------------------------------------------------

'''
food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza")
    elif(x.get()==1):
        print("You ordered a hamburger")
    elif(x.get()==2):
        print("You ordered a hotdog")
    else:
        print("huh?")

window = Tk()
# pizzaImage
# hamburgerImage
# hotdogImage
# foodImages = [pizzaImage, hamburgerImage, hotdogImage]
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], # adds text to radio buttons
                              variable=x,       # groups radiobuttons together if they share the same variable
                              value=index,      # assign each
                              padx=25,          # adds padding on x-axis
                              font=("Impact",50),
                              # image=foodImages[index],   # adds image to radiobutton
                              # compound= 'letf'  # adds image & text (left-side)
                              indicatoron=0,     # eliominate circle indicators
                              width=10,          # sets width of radio buttons
                              command=order      # sets command of radiobutton to function
                              )
    radiobutton.pack(anchor=W)  # wyrównanie do lewej strony
window.mainloop()
'''
# ------------------------------------------------
# sliding scale - skala przesuwana
# ------------------------------------------------
'''
def submit():
    print("The temperature is: "+str(scale.get())+" degrees C")


window = Tk()

# hotImage = PhotoImage()
# hotLabel = Label(image=hotImage)
# hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  # this is orientation of scale
              font=('Consolas',20),
              tickinterval=10,  # this adds numeric indicators for value
              # showvalue= 0,  # hide current value
              resolution= 5,  # przesuwanie co 5
              troughcolor= '#69EAFF',
              fg= '#FF1C00',
              bg= '#111111'
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])   # ustawienie domyślne
scale.pack()

button = Button(window, text='submit',command=submit)
button.pack()

window.mainloop()
'''
# ------------------------------------------------
# listbox = A listing of selectable text items within it's own container
# ------------------------------------------------
'''
def submit():
    print("You have ordered: ")
    # print(listbox.get(listbox.curselection())) # ona jest git gdy jest zaznaczana tylko jedna rzecz
    food = []

    for index in listbox.curselection():
        food.insert(index,listbox.get(index))
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size()) # dopasowuje rozmiar okna do ilości elementów

def delete():
    # listbox.delete(listbox.curselection()) # to pozwala usuwać tylko jedną rzecz
    for index in reversed(listbox.curselection()): # wybierać musimy od końca bo inaczej usuną się nie te indeksy
        listbox.delete(index)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg= "#F7FFDE",
                  font=("Constanria",35),
                  width=12,
                  selectmode=MULTIPLE # pozwala zazwnaczyć kilka rzeczy
                  )
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "garlic bread")
listbox.insert(4, "soup")
listbox.insert(5, "salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()
'''
# ------------------------------------------------
# wiadomości/ostrzeżenia
# ------------------------------------------------
'''
from tkinter import messagebox

def click():
    # messagebox.showinfo(title='This is an info message box', message='You are a person') # zwykła wiadomość
    # messagebox.showwarning(title='WARNING!', message='You have a VIRUS') # ostrzeżenie
    # messagebox.showerror(title='ERROR!', message='something went wrong :(') # info o błędzie
    # if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing?'): # to jest to okienko z
        # z ok lub anuluj xD
        # print('You do the thing!')
    # else:
    #     print('You canceled a thing!')
    # if messagebox.askretrycancel(title='ask retry cancel', message='Do you want retry the thing?'):  # to jest to okienko z
        # z zapytaniem czy coś spróbować jeszcze raz lub anuluj
        # print('You retried a thing!')
    # else:
    #     print('You canceled a thing!')
    # if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):  # to jest to okienko z
    #     z zapytaniem tak lub nie
        # print('I like cake too :D ')
    # else:
    #     print('Why do you not like cake? :(')
    # answer = messagebox.askquestion(title='ask question', message='Do you like pie? ') # zapytanie tak/nie
    # if(answer == 'yes'):
    #     print('I like pie too')
    # else:
    #     print('Why do you not like pie? ')
    answer = messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code? ', icon = 'warning')
    # icon powoduje chyba zmianę obrazka w pytaniu i dźwieku (too tylko chyba)
    if(answer==True):
        print('You like to code :D')
    elif(answer==False):
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question")
window = Tk()


button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()
'''
# ------------------------------------------------
# colorchooser
# ------------------------------------------------
'''
from tkinter import colorchooser # submodule

def click():
    color = colorchooser.askcolor()
    print(color) # wyświetli kolor który wybraliśmy kodem i kodem szesnastkowym
    colorHex = color[1]
    print(colorHex) # wyświetli kolor w kodzie hex
    window.config(bg=colorHex) # zmieniamy kolor background (tła)
    # window.config(colorchooser.askcolor()[1]) # alternatywny zapisa za pomocą jednej linii
window = Tk()

window.geometry("420x420")
button = Button(text='click me', command=click)
button.pack()

window.mainloop()
'''
# ------------------------------------------------
# text widget - functions like a text area, you can enter multiple lines of text
# ------------------------------------------------
'''
def submit():
    input = text.get("1.0",END) # to oznacza że od pierwszej linii do końca
    print(input)

window = Tk()

text = Text(window,
            bg="light yellow",
            font=("Ink Free",20),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="purple"
            ) # tworzy okno w którym można zapisywać tekst
text.pack()
button = Button(window, text = "submit", command=submit)
button.pack()

window.mainloop()
'''
# ------------------------------------------------
# filedialog - open and read the contents of a file
# ------------------------------------------------
'''
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:\\Python_nauka", title="Open file okay? ",
                                          filetypes=(("text files","*.txt"), # to jest ograniczenie do typu pliku :D 
                                          ("all files", "*.*")))
    # jeśli dodamy ścieżkę to folder w którym będziemy się pojawiać na początku będzie tym z ścieżki
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()
'''
# ------------------------------------------------
# filedialog - save a file
# ------------------------------------------------
'''
from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="D:\\Python_nauka",
                                    defaultextension='.txt', # domyślne rozszerzenie
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:    # to w przypadku gdyby przy zapisywaniu się rozmyślić i chcieć coś dopisać to to
        # nie wywali błędu tylko wróci do okienka w którym tekst był pisany 
        return
    filetext = str(text.get(1.0,END))
    # filetext = input("Enter some text I quess: ") #alternatywa do tego wyżej gdyby to wpisać tekst z konsoli
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
'''
# ------------------------------------------------
# menu bar - menu
# ------------------------------------------------
'''
def openFile():
    print("File has been opened! ")
def saveFile():
    print("File has been saved! ")
def cut():
    print("You cut some text! ")
def copy():
    print("You copied some text! ")
def paste():
    print("You pasted some text! ")
window = Tk()

# openImage = PhotoImage(file="") dodawanie zdjęcia i zapisywanie go w zmiennej openImage

menubar = Menu(window)
window.config(menu=menubar) # ustawiamy menu jako menubar

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli",15)) # w oknie menubar tworzymy fileMenu # tearoff = 0 usuwan linię z "----"
menubar.add_cascade(label="File", menu=fileMenu) # ustalamy nazwę i tworzymy listę rozwijaną dla fileMenu
fileMenu.add_command(label="Open", command=openFile,
                     # image=openImage, - by dodać zdjęcie
                     # compound='left'  - by zdjęcie nie zastąpiło tekstu tylko było z boku
                     ) # clickable option
fileMenu.add_command(label="Save", command=saveFile) # clickable option
fileMenu.add_separator() # by oddzielić save od exit
fileMenu.add_command(label="Exit", command=quit) # clickable option

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()
'''
# ------------------------------------------------
# frame = a rectangular container to group and hold widgets
# ------------------------------------------------
'''
window = Tk()

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN) # relief to taki 3d efekt (gdzie jest cień xD)
frame.pack(side=BOTTOM) # miejsce tak jakby wyśrodkowane 
# frame.place(x=100, y=100) # konkretne miejsce

Button(frame, text = "W", font=("Consolas", 20),width=3).pack(side=TOP)
Button(frame, text = "A", font=("Consolas", 20),width=3).pack(side=LEFT)
Button(frame, text = "S", font=("Consolas", 20),width=3).pack(side=LEFT)
Button(frame, text = "D", font=("Consolas", 20),width=3).pack(side=LEFT)

window.mainloop()
'''
# ------------------------------------------------
# creating new window
# ------------------------------------------------
'''
def create_window():
    new_window = Tk() # Toplevel() = new window 'on top' of other windows, linked to a 'bottom' window
    # czyli nasze główne okno będzie bottom level a to nowe będzie top level - gdy zamkniemy okno główne to to również
    # zostanie zamknięte - są połączone - myśleć o tym jak o grze " Jenga "
    # Tk() - new independent window - czyli nowe główne okno - i będą wtedy dwa okna główne - nie połączone ze sobą
    old_window.destroy() # instrukcja - przy stworzeniu nowego okna stare jest niszczone 

old_window = Tk()

Button(old_window, text="create new window", command=create_window).pack()

old_window.mainloop()
'''
# ------------------------------------------------
# creating tabs - zakładki - podstrony
# ------------------------------------------------
'''
from tkinter import ttk # moduł z kilkoma dodatkowymi widgetami

window = Tk()

notebook = ttk.Notebook(window) # widget taht manages a collection of windows/displays

tab1 = Frame(notebook)  # new frame for tab 1
tab2 = Frame(notebook)  # new frame for tab 2

notebook.add(tab1, text="Tab 1") # stworzyliśmy zakładki i ich nazwy
notebook.add(tab2, text="Tab 2")
notebook.pack(expand=True, fill="both")  # expand = expand to fill any space not otherwise used
# fill = fill space on x and y axis - pozwoli nam to by ramki powiększały się wraz z kodem 

Label(tab1, text="Hello, this is tab#1",width=50, height=25).pack()
Label(tab2, text="Goodbye, this is tab#2",width=50, height=25).pack()

window.mainloop()
'''
# ------------------------------------------------
# grid() - geometry manager that organizes widgets in a table-like structure in a parent
# grid działa jakby okno było podzielone na jedną dużą tabelę z wierszami i kolumnami
# ------------------------------------------------
'''
window = Tk()

titleLabel = Label(window, text="Enter your info", font=("Arial",25)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window, text="First name: ", width=20, bg="red").grid(row=1, column=0)
firstNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window, text="Last name: ",bg="green").grid(row=2, column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailNameLabel = Label(window, text="Email: ", bg="blue",width=30).grid(row=3, column=0)
emialNameEntry = Entry(window).grid(row=3,column=1)

submitButton = Button(window, text="Submit").grid(row=4, column=0, columnspan=2) # columnspan oznacza połączenie tak
# jakby dwóch kolumn by móc wyśrodkować to co chcemy

window.mainloop()
'''
# ------------------------------------------------
# progress bar - pasek ładowania
# ------------------------------------------------
'''
from tkinter.ttk import *
import time

def start():
    GB = 100
    download = 0
    speed = 1
    while(download<GB):
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100))+"%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update_idletasks() # to odświerza okno by wyświetlać postęp

window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack()

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()

button = Button(window, text="download",command=start).pack()

window.mainloop()
'''
# ------------------------------------------------
# canvas = widget that is used to draw graphs, plots, images in window
# ------------------------------------------------
'''
window = Tk()
canvas = Canvas(window, height=500, width=500)
# canvas.create_line(0,0,500,500, fill="blue", width=5) # linia na ukos
# canvas.create_line(0,500,500,0, fill="red", width=5)
# canvas.create_rectangle(50,50,250,250, fill="purple") # kwadrat
# canvas.create_polygon(250,0,500,500,0,500, fill="yellow", outline="black", width=5) # trójkąt
# points = [250,0,500,500,0,500]
# canvas.create_polygon(points, fill="yellow", outline="black", width=5)  # 2 sposób na trójkąt
# canvas.create_arc(0,0,500,500, style = PIESLICE, start=180, width=5) # ćwiartka okręgu/ łuk
canvas.create_arc(0,0,500,500,fill = "red",extent = 180, width=10)
canvas.create_arc(0,0,500,500,fill = "white",extent = 180,start=180, width=10)
canvas.create_oval(190,190,310,310, fill="white", width=10)
canvas.pack()
window.mainloop()
'''
# ------------------------------------------------
# key events
# ------------------------------------------------
'''
def doSomething(event):
    # print("You pressed: "+ event.keysym)
    label.config(text=event.keysym) # to wyświetla klawisze jakie naciskamy 

window = Tk()

window.bind("<Key>", doSomething) # w nawiasie <> podajemy jaki klawisz na klawiaturze nacisnąć aby wykonała się
# funkcja doSomething - "Return" oznacza ENTER a "Key" oznacza jakikolwiek klawisz
label = Label(window, font=("Helventica",100))
label.pack()
window.mainloop()
'''
# ------------------------------------------------
# mouse events
# ------------------------------------------------
'''
def doSomething(event):
    print("Mouse coordinates" + str(event.x)+","+str(event.y))

window = Tk()

# window.bind("<Button-1>", doSomething) # Button-1 - lewy przycisk myszy
# window.bind("<Button-2>", doSomething) # Button-2 - naciśnięcie środkowego przycisku myszy(scrolla)
# window.bind("<Button-3>", doSomething) # Button-3 - prawy przycisk myszy
# window.bind("<ButtonRelease>",doSomething) # po puszczeniu przycisku
# window.bind("<Enter>",doSomething) # Enter the window - koordynaty gdzie weszlismy do okna xD
# window.bind("<Leave>",doSomething)  # Leave the window
# window.bind("<Motion>",doSomething) # Where the mouse moved - gdy się poruszamy myszką
window.mainloop()
'''
# ------------------------------------------------
# drag and drop widgets in python - przenoszenie przedmiotów na oknie
# ------------------------------------------------
'''
from tkinter import *

def drag_start(event):
    widget = event.widget # ta komenda pozwala na ruch tym #Label na który aktualnie nacisneliśmy 
    widget.startX = event.x # wyznaczenie współrzędnych x gdzie nacisneliśmy na label (na kwadrat)
    widget.startY = event.y # wyznaczenie współrzędnych y gdzie nacisneliśmy na label (na kwadrat)

def drag_motion(event):
    widget = event.widget
    # poniższe całe wyrażenia dają nam nowe współrzędne
    x = widget.winfo_x() - widget.startX + event.x    # label.winfo_x - górny lewy róg współrzędne
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

label = Label(window, bg="red", width=10, height=5)
label.place(x=0,y=0)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100,y=100)

label.bind("<Button-1>",drag_start)
label.bind("<B1-Motion>",drag_motion) # B1-Motion - oznacza trzymanie lewego przycisku myszy i puszczenie go

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

window.mainloop()
'''
# ------------------------------------------------
# move image - porusznie się obrazkiem
# ------------------------------------------------

# to działa na label tylko:
'''
def move_up(event):
    label.place(x=label.winfo_x(), y = label.winfo_y()-10) # poruszanie się do góry za pomocą klawisza W
def move_down(event):
    label.place(x=label.winfo_x(), y = label.winfo_y()+10)
def move_left(event):
    label.place(x=label.winfo_x()-10, y = label.winfo_y())
def move_right(event):
    label.place(x=label.winfo_x()+10, y = label.winfo_y())
'''
'''
# to na canvas:
def move_up(event):
    canvas.move(myimage,0,-10)
def move_down(event):
    canvas.move(myimage, 0, +10)
def move_left(event):
    canvas.move(myimage, -10, 0)
def move_right(event):
    canvas.move(myimage, +10, 0)
window = Tk()
'''
'''
window.geometry("500x500")
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

myimage = PhotoImage(file='img.png')
label = Label(window, image=myimage)
label.place(x=0, y=0)
'''
# teraz to samo ale za pomocą canvas
'''
window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)
canvas = Canvas(window, width=500, height=500)
canvas.pack()

photoimage = PhotoImage(file='img.png')
myimage = canvas.create_image(0,0,image=photoimage, anchor = NW) # anchor dodajemy bo inaczej ucina obraz NW -North West

window.mainloop()
'''
# ------------------------------------------------
# simple 2D animation
# ------------------------------------------------
'''
from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVeliocity = 3 # ustawienie prędkości dla x
yVeliocity = 2 # ustawienie prędkości dla y

window = Tk()

canvas = Canvas(window,width=WIDTH, height=HEIGHT)
canvas.pack()

photo_space = PhotoImage(file='space.png')
my_image_space = canvas.create_image(0,0,image = photo_space, anchor=NW)

photo_ufo = PhotoImage(file='ufo.png')
my_image_ufo = canvas.create_image(0,0,image = photo_ufo, anchor=NW)

image_width = photo_ufo.width()
image_height = photo_ufo.height()

while True:
    coordinates = canvas.coords(my_image_ufo)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVeliocity = xVeliocity * (-1)
    if (coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0):
        yVeliocity = yVeliocity * (-1)
    canvas.move(my_image_ufo,xVeliocity,yVeliocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
'''
# wrzucienie Gita
# ------------------------------------------------
# animate multiple objects
# ------------------------------------------------
from tkinter import *
import time
from Ball import *

window = Tk()
WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white") # towrzymy dzieki klasie
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
basket_ball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volley_ball.move()  # włączamy piłkę do pętli oraz nadajemy jej funkcję move() z klasy Ball
    tennis_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()

