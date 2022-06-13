###################################################
# >> The Arithmetic Operations Magic Method
###################################################
# region

# We have magic methods for performing arithmetic operations between two objects - obj1 + obj2

class Example_Class:
    def __init__(self):
        pass


obj_1 = Example_Class()
obj_2 = Example_Class()

# print(obj_1 + obj_2)
# output:
# TypeError: unsupported operand type(s) for +: 'Example_Class' and 'Example_Class'

# endregion

###################################################
# >> Arithmetic Operations Magic Method - __add__(), __sub__(), __mul__()
###################################################
# region

# >> We will perform addition between two objects together, by implementing the __add__() method
# >> We will perform subtraction between two objects together, by implementing the __sub__() method
# >> We will perform multiplication between two objects together, by implementing the __mul__() method


class Add_Class:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Add_Class(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Add_Class(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Add_Class(self.x * other.x, self.y * other.y)


inst_A = Add_Class(10, 20)
inst_B = Add_Class(1, 2)

print(inst_A + inst_B)
# output:
# <__main__.Add_Class object at 0x000001D6CC63FBB0>

combined = inst_A + inst_B
print(combined.x)
# output: 11
print(combined.y)
# output: 22

combined = inst_A - inst_B
print(combined.x)
# output: 9
print(combined.y)
# output: 8

combined = inst_A * inst_B
print(combined.x)
# output: 10
print(combined.y)
# output: 40

# endregion

 