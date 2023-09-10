from abc import ABC

class Animal(ABC):

    def __init__(self, eat):
        self.eat = eat

    def eat(self):
        self.eat()

class Dog():

    def eat(self):
        print("Eating like a dog")

class Cat():
    def eat(self):
        print("Eating like a cat")


c1 = Animal
c2 = Dog
c3 = Cat
