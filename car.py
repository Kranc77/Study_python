class Car:      # klasa

    wheels = 4  # class variable - dla każdej klasy będzie to stała

    # special method - specjalna metoda tworząca obiekt?
    # konstruktor
    def __init__(self, make, model, year, color):
        # attributes - atrybuty
        self.make = make    # instance variable # unique value
        self.model = model  # instance variable # unique value
        self.year = year    # instance variable # unique value
        self.color = color  # instance variable # unique value

    # methods - metody (funkcje chyba)
    def drive(self):    # to w nawiasie to argument
        print("This "+self.model+" is driving")
    def stop(self):
        print("This "+self.model+" car is stopped")