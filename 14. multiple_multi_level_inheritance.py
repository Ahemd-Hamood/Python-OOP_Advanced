###################################################
# >> Multi-Level Inheritance
###################################################
# region

# As we know inheritance prevent code duplication and allows us to reuse our code.
class ClassA:  # Parent/Base Class
    # Methods
    # attributes
    pass


class ClassB(ClassA):  # Child/Derived/Sub Class
    # Methods
    # Attributes
    # And Class A Method and attributes
    pass


# The child ClassB inherit all the feature like method and attributes from the parent ClassA
# let's define another class called "ClassC" that inherit from ClassB

class ClassC(ClassB):
    # Methods
    # Attributes
    # And Class B,C Method and attributes
    pass

# >> Here the ClassC inherit all the features like method and attributes from the parent ClassB
# >> And ClassC inherit from the parent ClassA, this mean that ClassC inherit from both classes ClassB and ClassA

# We have a concept called "inheritance abuse" where a child class inherit from a parent class some feature that the child class don't need.

# Avoid deep multiple level inheritance, and use only one or two levels like above ClassC -> ClassB --> ClassA

# << Multi-Level Inheritance that you should avoid :-


class ClassA:
    pass


class ClassB(ClassA):
    pass


class ClassC(ClassB):
    pass


class ClassD(ClassC):
    pass


class ClassE(ClassD):
    pass


class ClassF(ClassE):
    pass

  # endregion

###################################################
# >> Multiple Inheritance
###################################################
# region


class FeatureA:
    def tool_1(self):
        print("Tool 1 from Feature A")

    def message(self):
        print("Message from FeatureA")

    def greet(this):
        print("Welcome from Feature A")


class FeatureB:
    def tool_2(self):
        print("Tool 2 from Feature B")

    def message(self):
        print("Message from FeatureB")

    def notification(self):
        print("notification from FeatureB")


class ManageFeatures(FeatureA, FeatureB):
    def greet(this):  
        print("Welcome from ManageFeatures")

# In python a child/sub/derived class can have multiple base/parent classes.
# The Multiple inheritance is where the ManageFeatures child class inherit all the features from both FeatureA and FeatureB parent classes
# Our child class will look up for methods base on inheritance order:
# >>  ManageFeatures(FeatureA, FeatureB) :  In method call it will look in the following order ManageFeatures -> FeatureA -> FeatureB
# >>  ManageFeatures(FeatureB, FeatureA) :  In method call it will look in the following order ManageFeatures -> FeatureB -> FeatureA
# while looking for a method, the first method occurrence will be executed, then terminate the look up process


MF = ManageFeatures()

MF.message()  # ManageFeatures will look for message() method first in itself, then FeatureA class (found it) terminate look up process
# output:
# Message from FeatureA

MF.notification()  # ManageFeatures will look for notification() method first in itself, then FeatureA class after that in the FeatureB class
# output:
# notification from FeatureB

MF.greet()  # ManageFeatures will look for greet() method first in itself, (found it) terminate look up process
# output:
# Welcome from ManageFeatures

MF.tool_1()
# output:
# Tool 1 from Feature A

MF.tool_2()
# output:
# Tool 2 from Feature B

# endregion
