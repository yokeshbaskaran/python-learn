# Exception handling
# - In Python, exception handling is used to handle runtime errors (exceptions) so that your program doesn’t crash unexpectedly.


# Errors:
# -------
# i) Runtime Error : Program starts running, but error happens during execution. => Logic/execution problem during running
# ii) Compile Time Error : Python detects the error before execution. => Wrong code syntax


# 🔹 Key Points
# ---------------------------
# 1. try        → code that may fail
# 2. except     → handles errors
# 3. else       → runs if no error
# 4. finally    → always executes
# 5. raise      → create an exception


# 🔹 Common Exceptions
# ---------------------------------------
#    Exception      	        Meaning
# ---------------------------------------
# 1. SyntaxError                Invalid syntax
# 2. ZeroDivisionError          Division by zero
# 3. ValueError                 Invalid value
# 4. TypeError                  Wrong data type
# 5. IndexError                 Invalid list index
# 6. NameError                  Variable not defined
# 7. KeyError                   Dictionary key not found
# 8. AttributeError             Invalid object attribute
# 9. FileNotFoundError          File does not exist
# 10. ModuleNotFoundError       Module not found
# 11. Exception                 Handles most exceptions


# Diff Between Error & Exception
# -------------------------------
#  - Error → Serious problem (syntax error, system error)
#  - Exception → Runtime problem that can be handled

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
