#python datatypes and varaibles
name = "Bhuvanakruthi P"
roll_no = 13
cgpa = 8.8
results = True


print("Name:", name)
print("Age:", roll_no)
print("CGPA:", cgpa)

#in bulit for finding length of string
print(len(name))

print(name[0])
print(name[-1])
print(name[0:])#here we can print full string

course="python /"programming"
print(course)#output is python "prgramming
# Notes:
# String -> Text
# Integer -> Whole number
# Float -> Decimal number
message='''
autopep8 can make are code look clean

we can give paragraph(string) in this
'''

#/n it breaks the sentence other part of the sentence appers in new line

#concatination
first = "bhuvana"
last = "kruthi"
full = first+""last 
#full=f"{first} {last} same output
#full=f"{len(first)} {2+2} 

#we can different funtion in built in python for example upper,lower,isdigital,etc
print(course.upper())
print(course.find("pro"))# output is 8
print(course.strip()) #removes space before and after string
print(course.replace("p","j")) 
print("pro" in course) #output is in boolean

#NUMBERS
print(10//3) #u get int

x = x+3
x += 3 #both are same 

x = input("x: ")
y = int(x) + 1
print(f"x: {x},y: {y}")
