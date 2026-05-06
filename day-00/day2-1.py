# Looping
# 1. For loop - The for loop is usually used when the number of iterations is known.
for i in "apple":
    print("value of i:", i)  # a, p, p, l,e

# range() - In Python, range() is a built-in function used to generate a sequence of numbers. It’s commonly used in loops (like for loops).
for i in range(10):
    print("value of i:", i)

for i in range(0, 10):
    print("value of i:", i)

for i in range(1, 11):
    n = i * 2
    result = str(i) + " x 2 = " + str(n)
    # print("value of i:", n)
    print(result)

for i in range(8 + 1, 15):
    print("---")
    print(i)

a = int(input("a:"))
b = int(input("b:"))
print("---")
for i in range(a + 1, b):
    print(i)

# print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# print odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 1:
        print(i)

# count the even/odd nums
odd_count = 0
even_count = 0
for i in range(1, 14):
    if i % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("even:", even_count)
print("odd_count:", odd_count)

# count num which div by 3 and 5
div_by_3 = 0
div_by_5 = 0
div_by_both = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        div_by_both += 1
        print("both", i)
    elif i % 3 == 0:
        div_by_3 = div_by_3 + 1
        print("by 3", i)
    elif i % 5 == 0:
        div_by_5 = div_by_5 + 1
        print("by 5", i)

print("div_by_3:", div_by_3)
print("div_by_5:", div_by_5)
print("div_by_both:", div_by_both)

# Q6. Write a program to compute the sum of the first 5 natural numbers
sum = 0
for i in range(1, 6):
    sum = sum + i
print("sum of i:", sum)

a = [1, 2, 3, 4, 5]  # list
for i in a:
    print(i)

# Q7. Write a program to read 10 numbers from the keyboard and find their sum and average.
a = []
for i in range(5):
    num = int(input("Enter value" + str(i + 1) + ":"))
    a.append(num)
print(a)

sum = 0
for i in a:
    sum = sum + i
avg = sum / len(a)
print(sum)
print("average", avg)

# display cube of number
a = int(input("enter value:"))
cube = 0
for i in range(1, a + 1):
    cube = i * i * i
    print("value of", i, ":", cube)

week = 3
day = 4
for i in range(1, week):
    print("week-", i)
    for j in range(1, day):
        print(" day-", j)

for i in range(5):
    print("*", end="")

# prints (*) patterns
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print("")

# prints (12345) patterns
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print("")
