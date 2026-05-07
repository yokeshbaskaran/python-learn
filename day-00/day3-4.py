# Polymorphism
# - it means: “Same method name, different behavior.”
# - The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types.
# - The key difference is the data types and number of arguments used in function.


# Examples
# ex-1
def add(a, b, c=10):  # default parameter - c when value not passed
    print(a + b + c)


add(8, 2)
add(8, 2, 20)


# ex-2: Method overloading
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dogs barks")


class Bird(Animal):
    def sound(self):
        print("Birds Sing")


dog = Dog()
dog.sound()

birds = Bird()
birds.sound()


# ex-3
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def area(self):
        l = 10
        b = 20
        print(l * b)
        # return 0


s1 = Rectangle()
s1.area()


# ex-3
class Person:
    def __init__(self, name):
        self.name = name
        # print("name:", self.name)


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def studentDetails(self):
        print("name:", self.name)
        print("grade:", self.grade)


# stu = Person("rocky")

student1 = Student("Rocky", "A+")
student1.studentDetails()


# ex-4:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printDetails(self):
        print("emp details:")
        print("Name:", self.name)
        print("salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, salary, dpt):
        super().__init__(name, salary)
        self.dpt = dpt

    def printDetails(self):
        print("Manager details:")
        print("Name:", self.name)
        print("salary:", self.salary)
        print("dpt:", self.dpt)


e1 = Employee("Govindan", 6000)
e1.printDetails()

print("---")
sam = Manager("Sammy", 45000, "Civil")
sam.printDetails()
