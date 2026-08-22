#functions

#we start with def keyword
#example

def add(a, b):
    print(a + b)

add(10, 20)

def greet():
    print("Hi there")
    print("Welcome aboard")
greet()

#Argumennts : takes  inputs (actual value for a given parameter)
def greet(first_name,last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
greet("bhuvana","kruthi")

#types of functions
def greet:
    print(f"Hi {name}")

print(greet("Bhuvana"))# output is none
#if we give return then we will not none when we give print statement

def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(15, 10))

#example 
def increment(num,by):
    return num + by
print(increment(2,1))

# we can also give default values i.e, by=1
#optional parameters should come after require parameters only

#example
def multiply(*numbers):
#function can accept any number ofarguments(*)
    total = 1
    for number in nummbers:
        total *= number
    return total

print(multiply(2,3,4,5))


