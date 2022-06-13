###########################################
# >> Instance Attributes
###########################################
# region

class My_Class:
    def __init__(self, x, y):
        self.x = x # this is a instance attribute
        self.y = y # this is a instance attribute

    def read_info(self):
        print(f"x:{self.x}, y:{self.y}, z:{self.z}")


# Above we define two attributes x and y, for MyClass Object in the constructor pf the MyClass Class.
# Now when ever we create a new MyClass Object instance, we have to provide these attributes by default, like this:
instance_1 = My_Class(10, 20)

# >> Also you can define or set other attributes after we create My_Class object instance

instance_1.z = 30

print(instance_1.x)
# output: 10
print(instance_1.z)
# output: 30

instance_1.read_info()
# output:
# x:10, y:20, z:30

# Attributes like x, y, z are called 'instance attributes' that belong to My_Class instances or objects
# We can create an independent variable attributes for each MyClass instance for example 'z' and 'w' attributes only belong to instance_1
# You can't access 'instance_1.z' and 'instance_1.w' attributes in other instance like below.

instance_2 = My_Class(1, 2)
print(instance_2.x)
# output:
# 1

print(instance_2.y)
# output:
# 2

# print(instance_2.z)
# output:
# AttributeError: 'My_Class' object has no attribute 'z'

# instance_2.read_info()
# output:
# AttributeError: 'My_Class' object has no attribute 'z'

# endregion

###########################################
# >> Class Object Attributes - static variables
###########################################
# region

print("#"*50)
# Class object attribute are defined at the class level and they are the same a cross all instance of a class object, mean they are shared among all instances
# Class object attributes can be accessed/red on class reference or an object instance reference.
# To access class object attributes within methods we use the self keyword or use the class name itself as following :-


class UserInfo:
    id = 1  # this is a class object attribute or class level attribute
    title = "Welcome" # this is a class object attribute or class level attribute

    def __init__(self, name, age):
        self.name = name  # this is an instance attribute
        self.age = age  # this is an instance attribute

    def get_info(self):
        print(f"A. ID: {self.id}, Name: {self.name}")
        print(f"B. ID: {UserInfo.id}, Name: {self.name}")


user1 = UserInfo("Adam", 24)

print(user1.name)
# output: Adam
print(user1.age)
# output: 24
print(user1.id)
# output: 1
print(user1.title)
# output: Welcome

user1.get_info()
# output:
# A. ID: 1, Name: Adam
# B. ID: 1, Name: Adam


print(UserInfo.id)
# output: 1
print(UserInfo.title)
# output: Welcome

# >> here we can't access instance attributes because we need an instance object access

# print(UserInfo.name)
# output: AttributeError: type object 'UserInfo' has no attribute 'name'
# print(UserInfo.age)
# output: AttributeError: type object 'UserInfo' has no attribute 'age'

# >> We can change the class attributes using class reference

UserInfo.id = 100
UserInfo.title = "dayoff"

print(user1.id)
# output: 100
print(user1.title)
# output: dayoff

print(UserInfo.id)
# output: 100
print(UserInfo.title)
# output: dayoff

# endregion

###########################################
# >> Class Attributes with different instances
###########################################
# region
print("#"*50)

# when we create an instance from a class object, only we make copy with all instance attributes and each instance refer to the main class attribute


class OtherClass:
    ref_no = 200

    def __init__(self, name, age):
        self.name = name
        self.age = age


# >> Take a copy from OtherClass and reference it to instance_A
instance_A = OtherClass("Adam", 33)

print(instance_A.name)
# output: Adam
print(instance_A.age)
# output: 33
print(instance_A.ref_no)
# output: 200

# >> create a new instance_A attribute called ref_no. which overwrite/override ref_no class attribute in instance_A
instance_A.ref_no = 1000

print(instance_A.ref_no)
# output: 1000

# >> Take a copy from OtherClass and reference it to instance_B
instance_B = OtherClass("David", 13)

print(instance_B.name)
# output: David
print(instance_B.age)
# output: 13
print(instance_B.ref_no)
# output: 200

# >> create a new instance_B attribute called ref_no. which overwrite/override ref_no class attribute in instance_B
instance_B.ref_no = 5000

print(instance_B.ref_no)
# output: 5000

# >> Take a copy from OtherClass and reference it to instance_C
instance_C = OtherClass("userC", 13)
instance_D = OtherClass("userD", 13)

print(instance_C.name)
# output: userC
print(instance_C.age)
# output: 13
print(instance_C.ref_no)
# output: 200

# Change the class attribute from all instances
OtherClass.ref_no = 1

print(instance_C.ref_no)
# output: 1

print(instance_D.ref_no)
# output: 1

instance_C.ref_no = 5000

print(instance_C.ref_no)
# output: 5000

# >> instance_D still have the class attribute, we didn't override ref_no to be an instance attribute
print(instance_D.ref_no)
# output: 1

print(instance_B.ref_no)
# output: 5000

print(instance_A.ref_no)
# output: 1000

instance_E = OtherClass("userD", 13)

print(instance_E.ref_no)
# output: 1

# endregion

# **************************************************************
# **************************************************************
# **************************************************************
# **************************************************************

###########################################
# >> Class Attribute - Example 1
###########################################
# region
print("#" * 50)


class Example_Class:
    default_value = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_default_value(self):
        return self.default_value


instance_A = Example_Class(10, 20)
instance_B = Example_Class(30, 40)
instance_C = Example_Class(50, 60)

print(instance_A.default_value)  # output: 1
print(instance_B.default_value)  # output: 1
print(instance_C.default_value)  # output: 1

print(instance_A.get_default_value())  # output: 1
print(instance_B.get_default_value())  # output: 1
print(instance_C.get_default_value())  # output: 1

print(Example_Class.default_value)  # output: 1

# >> override the class attribute from all instances
Example_Class.default_value = 500

print(instance_A.default_value)  # output: 500
print(instance_B.default_value)  # output: 500
print(instance_C.default_value)  # output: 500

print(instance_A.get_default_value())  # output: 500
print(instance_B.get_default_value())  # output: 500
print(instance_C.get_default_value())  # output: 500

print(Example_Class.default_value)  # output: 500

# >> In instance_A, Create a new instance attribute called 'default_value' which override the default_value class attribute
instance_A.default_value = 999

print(instance_A.default_value)  # output: 999
print(instance_B.default_value)  # output: 500
print(instance_C.default_value)  # output: 500

print(instance_A.get_default_value())  # output: 999
print(instance_B.get_default_value())  # output: 500
print(instance_C.get_default_value())  # output: 500

print(Example_Class.default_value)  # output: 500

# endregion

###########################################
# >> Class Attribute - Example 2
###########################################
# region


class Circle:
    # Class Object Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi  # or self.pi

    # Method
    def get_circumference(self):
        return self.radius * self.pi * 2

# >> Create an instance of te circle


my_circle_A = Circle()

print(my_circle_A.pi)
# output:
# 3.14

print(my_circle_A.radius)
# output:
# 1

print(my_circle_A.area)
# output:
# 3.14

print(my_circle_A.get_circumference())
# output:
# 6.28

# >> Create an instance of te circle

my_circle_B = Circle(30)

print(my_circle_B.pi)
# output:
# 3.14

print(my_circle_B.radius)
# output:
# 30

print(my_circle_B.area)
# output:
# 2826.0

print(my_circle_B.get_circumference())
# output:
# 188.4

# endregion
