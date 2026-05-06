# Looping
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
