# Looping
# 2. while loop - The while loop is usually used when the number of iterations is unknown.

# examples:
# 1.Print a number from 1 to 5 using while loop
a = 1
while a < 6:
    print(a)
    a += 1


# 2. Write a loop statement to print the following series # 10,20,30,40,50,60, .... 200
a = 10
while a < 200:
    print(a, end=",")
    a = a + 10

# 3. write a program to print first 10 natural numbers in reverse order
a = 10
while a > 0:
    print(a, end=" ")
    a = a - 1

# 4.write a program to find the factorial of a number
i = 3
fact = 1
while i > 0:  # 3>0    2>0     1>0    0>0 = false
    fact = fact * i  # 1*3=3  3*2=6   6*1=6
    i = i - 1  # 3-1=2  2-1=1   1-1=0
print(fact)
