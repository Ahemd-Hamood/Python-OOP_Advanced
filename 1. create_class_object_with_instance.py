########################################################
# >> What is Class ?
########################################################

# Class is a blue print for creating a new object
# An Object is an instance of a class

# >> Here x belongs to class/object called 'int'
x = 1
print(type(x))
# output:
# <class 'int'>

########################################################
# >> Create a Custom Class
########################################################

# To create a custom class, we start with a 'class' keyword then we give it our class a name like ClassA then we end it with coma :
# We use Pascal format as the naming convention where the fist letter of every word should be uppercase and separating words without using underscore My_Class -> MyClass

# class MyClass:

########################################################
# >> Defining a function inside our class
########################################################

# when we define a function inside our classes, we must have at least one parameter and by convention we call that parameter 'self'


class MyClass:
    def print_name(self):
        print("Welcome to MyClass")


########################################################
# >> Creating an instance from our class/object
########################################################

# to create a new instance of MyClass object we call the class like a function, then we assign it to a variable

inst_1 = MyClass()  # an instance reference to MyClass Object
inst_2 = MyClass()  # an instance reference to MyClass Object

# Now we access the print_name function, with inst_1 we use the dot operator to access out Class

inst_1.print_name()
# output:
# Welcome to MyClass

inst_2.print_name()
# output:
# Welcome to MyClass

print(type(inst_1))
# output:
# <class '__main__.MyClass'>

print(type(inst_2))
# output:
# <class '__main__.MyClass'>


########################################################
# >> The isinstance() function
########################################################

# The isinstance(instance_object, Class):Boolean :-
# function is used to check if an object is an instance of a given class

print(isinstance(inst_1, MyClass))
# output:
# True

print(isinstance(inst_1, int))
# output:
# False

########################################################
# >> An Example
########################################################


class MyClass:
    def func_A(self):
        print("MyClass in function A")

    def func_B(self):
        print("MyClass in function B")

# >> create a new instance/reference object


new_inst = MyClass()

new_inst.func_A()
# output:
# MyClass in function A

new_inst.func_B()
# output:
# MyClass in function B
