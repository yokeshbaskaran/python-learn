# Python Functions:

# 🔹 What is a Function?
# - A function is a block of code that runs when you call it.
# - Instead of writing the same code again and again, you put it inside a function and reuse it.


# - Python functions are one of the most important building blocks in programming. They help you organize code, reuse logic, and make programs easier to understand. Let’s walk through the basics in a simple way.


# Examples
def greet():
    print("Hello World")


greet()  # calling a function called greet


#  using return keyword in function
def greet():
    return "Hello World"


# calling a function called greet
greet()  # nthg returns
print(greet())  # prints the returned value.


# samples
def valueA():
    return 10


a = valueA()
print("value of a:", a)


# adding 2 values
def add():
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print("add of a,b:", a + b)


add()  # calling add() function


# Get a integer number from user and pass it to the function called findevenorodd(). Let the function print whether the number is even or odd.


def findevenorodd(msg):  # parameters - msg
    print("Message is:", msg)


findevenorodd("Hi I am from DPI!")  # arguments - value("hi i ...DPI!")


#  Get a integer number from user and pass it to the function called findpassorfail(). Let the function print whether the number is even or odd.


def findpassorfail(num):  # parameters - num
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


a = int(input("Enter odd or even number:"))
findpassorfail(a)  # arguments -a

# Get input for a and b and pass it to the function called printrange() let the function print numbers from a to b.


def printrange(a, b):
    for i in range(a, b):
        print(i)


a = int(input("starting value:"))
b = int(input("ending value:"))
printrange(a, b)

# => Set s_username="EMC" s_password="123"
# Get input for uname and password and Create a function called validate. If uname and password matches the function should return true else false.


def validate():
    if s_username == username and s_pwsd == password:
        print("Correct! Logined")
        return True
    else:
        print("InCorrect! Not Logined")
        return False


s_username = "EMC"
s_pwsd = "123"

username = input("enter username:")
password = input("enter password:")
a = validate()
print("value of a:", a)

# 6)(a+b)*c - Get input for a and b and function called add() which should return the sum of a and b and multiply that sum with c


def add(n1, n2):
    num = n1 + n2
    print("added value:", num)
    return num


a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

result = add(a, b)
final = result * c
print("final:", final)
