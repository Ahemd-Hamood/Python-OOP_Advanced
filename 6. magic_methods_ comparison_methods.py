###################################################
# >> The Compare Objects - Magic Method
###################################################
# region

# We use the compare methods to compare two objects, like obj1 == obj2, obj1 > obj2, ..

class Example_Class:
    def __init__(self, x, y):
        self.x = x
        self.y = y


inst_A = Example_Class(1, 2)
inst_B = Example_Class(1, 2)

print(inst_A == inst_B)
# output:
# False

# We get False because by default python compare operator compares the references or addresses of these two object in memory
# inst_A and inst_B are referencing to different objects in memory, we will use the compare methods to solve our comparison


# endregion

###################################################
# >> Comparison magic methods: __eq__(), __gt__(), __ne__(), __lt__(), __le__(), __ge__()
###################################################
# region
print("#" * 50)

# >> The __eq__(self, other) equal magic method to compare attributes are equal between two object
# >> The __gt__(self, other) equal magic method to compare attributes are greater than between two object
# >> The __ne__(self, other) equal magic method to compare attributes are not equal between two object
# >> The __lt__(self, other) equal magic method to compare attributes are less than between two object
# >> The __le__(self, other) equal magic method to compare attributes are less or equal between two object
# >> The __ge__(self, other) equal magic method to compare attributes are greater or equal between two object


class Compare_Class:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y


obj_A = Compare_Class(1, 2)
obj_B = Compare_Class(1, 2)


print(obj_A == obj_B)  # the equal comparison will invoke the __eq__ magic method
# output:
# True

# the greater than comparison will invoke the __gt__ magic method
print(obj_A > obj_B)
# output:
# False

# the not equal comparison will invoke the __ne__ magic method
print(obj_A != obj_B)
# output:
# False

obj_A = Compare_Class(5, 6)
obj_B = Compare_Class(1, 3)

# the greater than comparison will invoke the __gt__ magic method
print(obj_A > obj_B)
# output:
# True

# >> the following comparison will work without the  __lt__() method
# the less than comparison will invoke the __gt__ magic method
print(obj_A < obj_B)
# output:
# False

# the not equal comparison will invoke the __ne__ magic method
print(obj_A != obj_B)
# output:
# True

obj_A = Compare_Class(5, 6)
obj_B = Compare_Class(20, 40)

# the less than comparison will invoke the __gt__ magic method
print(obj_A < obj_B)
# output:
# True


# endregion
