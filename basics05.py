class Car:
    def __init__(self,model,year,for_sale): #inorder to construct objects
        self.model=model
        self.year=year
        self.for_sale=for_sale

#you can add the above part in seperate file and access class Car
#import Car from car

car1=Car("bmw",2025,False)
car2=Car("Corvette",1984,True)

print(car1.model)
print(car1.year)
print(car1.for_sale)

#
    def drive(self):
        print("you drive the car")
        # print(f"you drive the {self.model} {self.year}")
car1.drive()

class Student:

    class_year=2024#class variable
    #can accessed ny student1,student2,Student
    num_students=0
    #we can caluculate no of students
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_students += 1

student1= Student("bhuvana",18)
student2 = Student("Poorna",19)

print(student1.name)
print(Student.class_year)
print(Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")


#Object oriented programming
#inheritance
class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Mouse(Animal):
    pass


dog = Dog("scooby")
cat = Cat("dooby")
mouse = Mouse("mike")

print(dog.name)
dog.eat()
print(dog.is_alive)
dog.sleep()


#multiple inheritance
class Animal:

    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey:
    def flee(self):
        print("this animal is fleeing")

class Predator:
    def hunt(self):
        print("this animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

rabbit = Rabbit("Ruby")
hawk = Hawk("honey")
fish = Fish("Nemo")

fish.flee()
fish.hunt()