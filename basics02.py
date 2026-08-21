#boolean
bool(0) #output is false
bool(1) #output is true
#when we give any number we get true

#Primitive ideas
name="Bhuvana"
print(name[-1:1])

#conditional statements
temp = 35
if temp > 30:
    print("it is warn")
    print("drink cool water")
elif temp > 20:
    print("Its nice")
else:
    print("its cold")
print("done")


#example 2
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")

# Example 3
#Using and, or, not

age = 20
has_id = True
is_banned = False

# AND condition
if age >= 18 and has_id:
    print("Eligible for entry")
else:
    print("Not eligible for entry")

# OR condition
attendance = 80
sports_quota = True

if attendance >= 75 or sports_quota:
    print("Eligible for exam")
else:
    print("Not eligible for exam")

# NOT condition
if not is_banned:
    print("Access granted")
else:
    print("Access denied")

#example 4
if 10=="10"
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")


#Loops:
# Example 1: Print numbers from 1 to 5

for i in range(1, 6):
    print(i)


for number in range(1,10,2):
    print("Attempt",number,numbber*".")

succesful = True
for number in range(3):
    print("Attempt")
    if succesful:
        print("succesful")
        break
else:
    print("attempted 3 times and failed")

#Nested  loops
for x in range(5):
    for y in range(4):
        print(f"{x},{y}")

for x in "Python"
    print(x)


for x in "[1,2,3,4]"
    print(x)

# Example 7: Iterate through a list

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

#while loop
num = 100
while num > 0:
    print(num)
    num //= 2

command=""
while command != "quit"
    command= input(">")
    print("ECHO",command)
# if the input is quit then the program will terminate

count=0
for i in range(1,10)
    if i % 2 ==0:
        count +=1
        print(i)
print(f"we have {count} even number")