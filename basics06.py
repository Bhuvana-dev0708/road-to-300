#abstract classes
from abc import ABC,abstract method

class Vehicle(abc):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass
        
class Car(Vehicle):

    def go(self):
        print("you drive your car")

    def stop(self):
        print("you stop the car")

class Motorcycle(Vehicle):

    def go(self):
        print("you drive your motorcycle")

    def stop(self):
        print("you stop the motorcyle")

class Boat(Vehicle):
    def go(self):
        print("you drive your boat")

    def stop(self):
        print("you stop the boat")


#Super

class Circle:
    def __init__(self,color,filled,radius):
        self.color = color
        self.filled = filled
        #super().__init__(color,filled)
        self.radius = radius

class Square:
    def __init__(self,color,filled,width):
        self.color = color
        self.filled = filled
        #super().__init__(color,filled)
        self.width = width


class Triangle:
    def __init__(self,color,filled,width,height):
        self.color = color
        self.filled = filled#noneed write this 2 lines when we write super
        #super().__init__(color,filled)
        self.width = width
        self.height = height

circle = Circle(color = "red", filled = True , radius=5)
sqaure=Square(color="blue",filled =True,width=7)
triangle=Triangle(color="yellow",filled=False,width=9,height=5)

print(square.color)