# Python Collections (Arrays):-
#  - There are four collection data types in the Python programming language:

# 1. List is a collection which is ordered and changeable. Allows duplicate members.
# 2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# 4. Dictionary is a collection which is ordered ** and changeable. No duplicate members.

# 1. list -[]
a = [1, 2, 3, 4, 5]
print("type a", type(a))  # <class 'list'>

# .append()
a.append(77)
a.append("hi")
a.append(True)
a.append(77)
print(a)
print(a[0])  # index starts at 0

# .insert()
b = [1, 2, 3, 4, 5]
# b.insert(2, 25)
# print(b)

# .pop()
b[0] = 20
print(b)
b.pop()
b.pop(0)  # index number
print(b)

# .extend()
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)
print(l2)
