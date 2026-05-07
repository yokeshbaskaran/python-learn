# Encapsulation
#  - Python, it means bundling data (variables) and methods (functions) that operate on that data into a single unit (class) and restricting direct access to some parts of the object.

# 🔹 Types of Access in Python

# | Access Type | Syntax  | Meaning                                      |
# | ----------- | ------- | -------------------------------------------- |
# | Public      | `var`   | Accessible anywhere                          |
# | Protected   | `_var`  | Should not be accessed directly (convention) |
# | Private     | `__var` | Name mangled to restrict access              |


# example -1:
class Company:
    def __init__(self):
        self._companyName = "Google"
        # self.__companyName = "Google"

    # def companyName(self):
    #     print(self.__companyName)


res = Company()
# res.companyName()
# print(res.__companyName)  # cannot access the private variables
print(res._companyName)


class b(Company):
    pass


b1 = b()
b1._companyName = "hi"
print("b1:", b1._companyName)
