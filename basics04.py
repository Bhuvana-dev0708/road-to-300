#Python classes

class Student:
    name = "Kruthi"
#name is an attribute (variable inside a class)
s1 = Student()#object

print(s1.name)


class Computer:

    def config(self):
        print("i7,16gb,1TB") 

com1 = Computer()#object
com2 = Computer()

Computer.config(com1)
com1.config()#both the syntax guves same output but we usually use second one
com2.config()


#using init(special method)
class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is",self.cpu,self.ram) 

com1 = Computer('i5',16)#object
com2 = Computer('Ryzen 3',8 )


com1.config()#both the syntax guves same output but we usually use second one
com2.config()

