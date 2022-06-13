###################################################
# >> Inheritance Methods
###################################################
# region

# >> What is the inheritance in Python?
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# In multiple class you may have similar methods which both classes have in common, instead of repeating the same method in both class
# simply we can use inheritance that one class inherit from another class

# To apply inheritance we add open/closing parenthesis after our class name like this class ClassName(inherit_from_1, inherit_from_2, ...)

from inspect import Attribute


class Animal:  # This is Parent/Base Class
    def eat(self):
        print("Eat")

    def move(self):
        print("Move")


class Fish(Animal):  # This is Child/Derived/Sub Class
    def swim(self):
        print("Swim")
    # def eat(self): # this method comes from the Animal Class
    # def move(self): # this method comes from the Animal Class


# The Fish class/child class inherit from the Animal class/base class both eat() and see classes
# Here Fish(Animal): The Animal parent class don't inherit anything from the Fish child class
obj1 = Fish()

obj1.swim()  # output: Swim
obj1.eat()  # output: Eat
obj1.move()  # output: Move

obj2 = Animal()
obj2.eat()  # output: Eat
obj2.move()  # output: Move
# obj2.swim()  # output: AttributeError: 'Animal' object has no attribute 'swim'

# endregion

###################################################
# >> Inheritance Attributes
###################################################
# region
print("#"*50)


class ClassA:  # this is parent/base class
    def __init__(self):
        self.name = "adam"
        self.age = 44

    def print_info(self):
        print(f"The name is {self.name}, ang age is {self.age} years old.")


class ClassB(ClassA):
    def greet(self):
        print(f"Welcome {self.name}")


CB = ClassB()

print(CB.name)  # output: adam
print(CB.age)  # output: 44

CB.print_info()
# output:
# The name is adam, ang age is 44 years old.

CB.greet()
# output:
# Welcome adam

# endregion

###################################################
# >> isinstance() and issubclass() build-in methods
###################################################
# region
print("#" * 50)


class Animal:
    pass


class Cat(Animal):
    pass


cat1 = Cat()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# The isinstance() method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >> The isinstance() method tell us if an object is instance of a given class or of sub-class

# Here cat1:Animal is an instance of sub-class Animal
print(isinstance(cat1, Animal))
# output:
# True

# Here cat1:Cat is an instance or case class of Cat
print(isinstance(cat1, Cat))
# output:
# True

_Animal = Animal()

# Here _Animal:Animal is an instance of Animal
print(isinstance(_Animal, Animal))
# output:
# True

# Here _Animal:Cat is not an instance of Cat
print(isinstance(_Animal, Cat))
# output:
# False

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# The issubclass() method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >> The issubclass() method accept two classes, it return wether class is a sub-class from another class or is the same

class Animal:
    pass


class Cat(Animal):
    pass

# is Cat a sub-class of Animal
print(issubclass(Cat, Animal))
# output:
# True

# is Animal a sub-class of Cat
print(issubclass(Animal, Cat))
# output:
# False

# is Animal the same as Animal
print(issubclass(Animal, Animal))
# output:
# True

# is Cat the same as Cat
print(issubclass(Cat, Cat))
# output:
# True

# The Animal is a sub-class of object, which inherit directly from the object class
print(issubclass(Animal, object))
# output:
# True

# The Cat is a sub-class of object, which inherit in-directly from the object class thru the Animal class
print(issubclass(Cat, object))
# output:
# True

# endregion

###################################################
# >> The Object Class
###################################################
# region
print("#" * 50)


class NewClassA:
    pass


class NewClassB(NewClassA):
    pass

# Every class in python inherit from a class called 'object' -> class NewClass(object)
# The object class is the base class for all classes in python,
# all classes inherit from the object class directly or in-directly from a sub-class

# >> if we check if NewClass is instance of the class object


new_class_b = NewClassB()

# >> here new_class_b:NewClassB instance inherit the object class in-directly from the NewClassA -->  NewClassB(NewClassA) then NewClassA(object)
print(isinstance(new_class_b, object))
# output:
# True


new_class_a = NewClassA()

# >> here new_class_a:NewClassA inherit the object class directly from itself -->  NewClassA(object)
print(isinstance(new_class_a, object))
# output:
# True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Creating an empty object using the object() build-in function
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# >> inside the class object we have magic methods that every class in python has.

o = object()

# o.__dir__
# o.__sizeof__
# o.__eq__
# o.__format__
# ....

# >> If you want to check the following class inherit all magic methods from the object class just inspect the dot operator


class NewClassA:
    pass


class_a = NewClassA()
# class_a.__dir__
# class_a.__sizeof__
# class_a.__eq__
# class_a.__format__
# ....


# endregion
