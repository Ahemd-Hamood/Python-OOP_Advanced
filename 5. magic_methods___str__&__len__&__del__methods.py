###################################################
# >> Magic Methods
###################################################
# region

# Magic methods are  methods that have two underscores at the beginning and end of their name __####__
# Magic Methods are behavior methods are called automatically by python interpreter depend on how we use our objects/instances and classes.

# For example the __init__() Magic method "constructor initializer" is called automatically by python interpreter when we create a new object instance from our class
# instance = My_Class() --> here python interpreter automatically will call the __init__ method and pass our initial values to it.

class My_Class:
    def __init__(self, x, y):
        print("The __init__() method called")
        self.x = x
        self.y = y


# >> Now we create a new instance from MyClass object/class
instance_A = My_Class(2, 3)

# output:
# The __init__() method called

# Also when we try to print or call our variable instance_A reference, python interpreter automatically will call a magic method called '__str__()'

print(instance_A)
# output:
# <__main__.My_Class object at 0x000001B235C67D60>


# endregion

###################################################
# >> The __str__(self) behavior - Magic Method
###################################################
# region

# The __str__() magic method behavior is called when we call an object instance reference or convert an object instance reference into a string.
# If we try to call an object instance using print() method, this will try to convert our object into a string
# print(instance_A) --> <__main__.My_Class object at 0x000001B235C67D60>
# lets change the output above by overriding the __str__ method.
# The __str__() magic method will be called if we try to call or convert an object into a string. this will happen if we call an object inside the print() method
# The __str__() magic method must return a string type representation in order to work

class Str_Class:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # here we override __str__ method, with our own implementation
        return f"The __str__ method called: x:{self.x}, y:{self.y}"


str_instance = Str_Class(33, 44)

# here we are converting str_instance to string, which it will invoke the __str__ method automatically

print(str_instance)
# output:
# __str__ method called: x:33, y:44

print(str(str_instance))
# output:
# __str__ method called: x:33, y:44

# endregion


###################################################
# >> The __len__(self) and  __del__(self) behavior - Magic Methods
###################################################
# region

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, author: {self.author}, pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")
        self.title = None
        self.author = None
        self.pages = None


book = Book("Python Rocks!", "Jose Portilla", 159)

# >> This this will call the __str__ magic method
print(book) 
# output:
# Title: Python Rocks!, author: Jose Portilla, pages: 159


# >> This this will call the __len__ magic method
print(len(book))
# output:
# 159

# >> This this will call the __del__ magic method
del book 
# A book is destroyed

# endregion
