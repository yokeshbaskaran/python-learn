# Exception handling
# - In Python, exception handling is used to handle runtime errors (exceptions) so that your program doesn’t crash unexpectedly.

# 🔹 Key Points
# - try → code that may fail
# - except → handles errors
# - else → runs if no error
# - finally → always executes
# - raise → create an exception

# ex-1
print("hi")
print("bye")
# printt("bro")  # NameError:- compile time error(syntax based)

# ex-2
a = 10
b = 20
print(a + a)  # logical error -> a + b

# ex-3
a = int(input())
b = int(input())
# enters value in b = hi -> ValueError: invalid literal for int() with base 10: 'ss' #runtime error
print(a + b)

# ex-4
try:
    a = int(input())
    b = int(input())
    # enters value in b = hi -> ValueError: invalid literal for int() with base 10: 'ss' #runtime error
    print(a / b)
except Exception:
    print("Enter integer(numbers) value like 1 or 2!")

# ex-5
try:
    a = int(input())
    b = int(input())
    # enters value in b = hi -> ValueError: invalid literal for int() with base 10: 'ss' #runtime error
    print(a / b)
except Exception as e:
    print("Enter integer(numbers) value like 1 or 2!", e)

# ex-6
try:
    a = int(input())
    b = int(input())
    c = input()
    # print(d)
    # print(c / a)  # TypeError: unsupported operand type(s) for /: 'str' and 'int'
except ValueError as e:  # works only for valueError
    print("ValueError:", e)
except TypeError as e:  # works only for valueError
    print("TypeError:", e)
except Exception:  # works for all error when occured
    print("Error:")
finally:
    print("done")
