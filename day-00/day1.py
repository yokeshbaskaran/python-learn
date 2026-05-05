# 1. print in python
print("Python is here")
# Python is here
print(2 + 4)
6

# 2. variables
a = 6
b = 4
print(a + b)
10

# 3. type() -> gives type of variables
print(type(a))
# <class 'int'>

a = "10"
print(a)
10
print(type(a))
# <class 'str'>

# 4. int usage in string value
a = "10"
b = "12"
print(a + b)

a = int("10")
b = int("10")
print(a + b)  # 20

# 5. input from user
# sample1
a = input()
b = input()
c = a + b
print("value of c:", c)  # 10 + 20 = 1020 (saves as string)

# sample2
a = int(input("value of a:"))
b = int(input("value of b:"))
c = a + b
print("value of c:", c)  # 10 + 20 = 30

# sample3
name = input("enter name:")
age = input("enter age:")
address = input("enter address:")
print("My name is:", name)
print("My address is:", address)

# sample4
a = int(input("enter value1:"))
b = int(input("enter value2:"))
c = int(input("enter value3:"))
mutliply = a * b * c
add = a + b + c
division = mutliply / add
print("output:", division)

# sample5
name = input()
score = int(input())
dpt = input()
print("My name is:", name)
divided = score / 10
print("My score is:", divided, "/10")
# divided = str(score / 10)
# print("My score is:", divided + "/10")
print("My dpt is:", dpt)
