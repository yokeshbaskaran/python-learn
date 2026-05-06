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
