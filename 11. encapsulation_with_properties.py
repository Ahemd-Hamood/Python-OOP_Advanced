###################################################
# >> Encapsulate Attributes with property
###################################################
# region

class Product:
    def __init__(self, price):
        self.price = price


obj_1 = Product(23)

print(obj_1.price)
# output:
# 23

obj_1 = Product(-99)

print(obj_1.price)
# output:
# -99

# >> As you see above we give a negative price, the python interpreter will execute that without any problems
# >> So we need to make sure that our price can not have a negative value we many solutions :-

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Solution 1 - Define private __price and __setter/getter price methods
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# region

# We will make our price private and provide a setter method that will run during initialization __init__, then will check our price value
# and also we will have a getter method that will return our private price, the following solution is consider 'unPythonic'
# unPythonic means that our code implementation is not using the best python practice, or it's not using the full python language features the fullest potential


class Product_S1:
    def __init__(self, price):
        self.__set_price(price)

    def __set_price(self, val):
        if val < 0:
            raise ValueError("Price can not be negative")
        self.__price = val

    def get_price(self):
        return self.__price


P1 = Product_S1(22)

# P1.__set_price(33)
# output:
# AttributeError: 'Product_S1' object has no attribute '__set_price'. Did you mean: 'get_price'?

print(P1.get_price())
# output: 22

# >> If you try to pass a negative price value, an error will be raised

# P1 = Product_S1(-34)
# output:
# ValueError: Price can not be negative

# endregion


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Solution 2 - Define a build-in property Function
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# region

# A property is an object that sits in front of an attribute and allows us to get or set the value of that attribute
# We use a build-in property(fget, fset, fdel, doc) function, that takes four parameters and all of them are optional :-
# - First Parameter : is a function for getting the value of an attribute
# - Second Parameter : is a function for setting the value of an attribute
# - Third Parameter : is a function for deleting that attribute
# - Fourth Parameter : is for documentation

# >> The property function will return a property object, which it will use both fget and fset functions for reading and writing our attribute
# when we set our attribute the value we assign to it will be pass into the setter function
# and when we get our attribute value we retrieve it or return it from the getter function

class Product_S2:
    def __init__(self, price):
        self.__set_price(price)

    def __set_price(self, val):  # you can make this method public
        print("Inside Price Setter")
        if val < 0:
            raise ValueError("Price can not be negative")
        self.__price = val

    def __get_price(self):  # you can make this method public
        print("Inside Price Getter")
        return self.__price

    price = property(__get_price, __set_price)


P2 = Product_S2(100)
# output:
# Inside Price Setter

print(P2.price)
# output:
# Inside Price Getter
# 100

# >> We set the price attribute, but here our value is passed into property.__set_price(25) for validation

P2.price = 25
# output:
# Inside Price Setter

print(P2.price)
# output:
# Inside Price Getter
# 25

# P3 = Product_S2(-89)
# output:
# > Inside Price Setter
# > ValueError: Price can not be negative

# P2.price = -99
# output:
# > Inside Price Setter
# > ValueError: Price can not be negative

# endregion

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Solution 3 - Using a property decorator @property
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# region
print("#" * 50)

# We can apply a property decorator '@property' above the getter method, and @<attribute_name>.setter above the setter method
# When we assign a getter method with '@property' python interpreter will automatically create a property object called 'price'
# When we assign a setter method with '@price.setter' python interpreter will consider this method as the setter method

# Note:
# When we get or set our attribute inside our getter and setter functions, we must make our attribute private
# or you are going to get an error 'RecursionError: maximum recursion depth exceeded in comparison'


class Product_S3:
    def __init__(self, name, price):
        self.item_name = name
        self.price = price

    @property
    def price(self):  # here a getter method
        print("Inside Price Getter")
        return self.__price  # this will set the price attribute

    @price.setter
    def price(self, val):  # here the setter method
        print("Inside Price Setter")
        if val < 0:
            raise ValueError("Price can not be negative")
        self.__price = val  # this will set the price attribute

    @property
    def item_name(self):  # here a getter method
        print("Inside item_name Getter")
        return self.__item_name  # this will get the item_name attribute

    @item_name.setter
    def item_name(self, val):  # here the setter method
        print("Inside item_name Setter")
        if val == '':
            raise ValueError("You must specify a name")
        self.__item_name = val  # this will set the item_name attribute

    # price = property(price_getter, price_setter)
    # item_name = property(item_name_getter, item_name_setter)


PA = Product_S3("Apple", 33)
# output:
# Inside item_name Setter
# Inside Price Setter

print(PA.item_name)
# output:
# Inside item_name Getter
# Apple

print(PA.price)
# output:
# Inside Price Getter
# 33

PA.item_name = "iPad"
# output: Inside item_name Setter
PA.price = 899
# output: Inside Price Setter

print(PA.item_name)
# output:
# Inside item_name Getter
# iPad

print(PA.price)
# output:
# Inside Price Getter
# 899

# PA.price = -33
# output: Inside Price Setter
# ValueError: Price can not be negative

# PA.price = ""
# output: Inside item_name Setter
# # ValueError: You must specify a name

# PB = Product_S3("", 33)
# output:
# Inside item_name Setter
# ValueError: You must specify a name

# PB = Product_S3("ABC", -87)
# output:
# Inside Price Setter
# ValueError: Price can not be negative


# endregion

# endregion

###################################################
# >> Create Read-only Property
###################################################
# region

class Product_S4:
    def __init__(self):
        pass

    @property
    def price(self):  # here a getter method
        print("Inside Price Getter")
        return 66

    @property
    def item_name(self):  # here a getter method
        print("Inside item_name Getter")
        return "Default"


PP = Product_S4()

print(PP.item_name)
# output:
# Inside item_name Getter
# Default

print(PP.price)
# output:
# Inside Price Getter
# 66

PP.item_name = "Screen"
# output:
# AttributeError: can't set attribute 'item_name'

PP.price = 45
# output:
# AttributeError: can't set attribute 'price'

# endregion
