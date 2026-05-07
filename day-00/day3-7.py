# 7. File Handling

my_file = open("data.txt")
print("file:", my_file)
content = my_file.read()  # reads the data inside a file
print(content)

my_file = open("data.txt", "w")  # it overrides with value
my_file.write("Hi \n")
my_file.write("bye!")

my_file2 = open("data.txt", "a")  # appends(add at end not overrides)
my_file2.write("\n last value!!!")
my_file2.close()

with open("data.txt", "w") as f:
    f.write("Hello")

f = open("data.txt", "r+")
print(f.readline())  # reads the first line
print(f.readline())  # reads the second line
print(f.readline())  # reads the third line and vice versa
