# Conditions (if/else)
age = int(input("enter ur age:"))
if age > 18:
    print("You are egilible to vote!")
else:
    print("You are not egilible to vote!!!")

# Comparison Operators
# 1. boolean value - True / False = python,js are case sensitive
data = True
if data:
    print("it is true")
else:
    print("it is false")

data = False
if data == False:
    print("it is false")
else:
    print("it is true")

name = input("enter friend name:")
if name == "Priya":
    print("Surya meets priya")
else:
    print("Surya meets meghna")

# 2. greater than(>) and less than (<)
mark = int(input("enter marks:"))
# if mark > 35:
if mark >= 35:
    print("Pass")
else:
    print("Fail!")

income = int(input("enter income:"))
if income > 7000:
    print("got a scholar")
else:
    print("got no scholar!")

sample = int(input("enter num:"))
if sample % 2 == 0:
    print("divided by 2")
else:
    print("not divided by 2")

sample = int(input("enter num:"))
if sample % 3 == 0:
    print("divided by 3")
else:
    print("not divided by 3")
