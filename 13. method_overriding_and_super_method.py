###################################################
# >> Inheritance with method overriding - initialize parent constructor using super keyword
###################################################
# region
print("#" * 50)

# When we have two similar methods in different classes, parent and child classes
# the child class will replace any similar method that exist in the parent class including the __init__() method

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> override the __init__() method in Parent class with it's attribute
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class PersonA:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def info_view(self):
        print(f"ID: {self.id}, Name: {self.name}")


class EmployeeA(PersonA):
    def __init__(self, title):
        self.title = title

    def print_title(self):
        print(f"Title: {self.title}")


# >> the moment you create Employee_1 instance object the __init__() method in EmployeeA Class will override/rewrite/remove the __init__() method from the PersonA Class
Emp1 = EmployeeA("My Title")

Emp1.print_title()
# output:
# Title: My Title

# Emp1.info_view()
# output:
# > AttributeError: 'Employee_1' object has no attribute 'id'
# > AttributeError: 'Employee_1' object has no attribute 'name'

# print(Emp1.id)
# output:
# > AttributeError: 'Employee_1' object has no attribute 'id'

# print(Emp1.name)
# output:
# > AttributeError: 'Employee_1' object has no attribute 'name'

print(Emp1.title)
# output:
# My Title

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> To inherit and initialize the parent class attributes we use the super().__init__()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("#" * 50)

# we call this method overriding, to execute the original method in the parent class instead from the child class
# We use a method called super() method, we use it to call any method in the parent class from the child class
# The super() method provide the super/parent class methods and attributes


class PersonB:
    def __init__(self, id, name):
        print("PersonB_Constructor")
        self.id = id
        self.name = name

    def info_view(self):
        print(f"ID: {self.id}, Name: {self.name}")


class EmployeeB(PersonB):
    def __init__(self, id, name, title):
        print("EmployeeB_Constructor")
        self.title = title
        super().__init__(id, name)  # here we call the parent class PersonB __init__() method

    def print_title(self):
        print(f"Title: {self.title}")


NewEmp = EmployeeB(1, "Adam", "My Title")
# output:
# EmployeeB_Constructor
# PersonB_Constructor

NewEmp.print_title()
# output:
# My Title

NewEmp.info_view()
# output:
# ID: 1, Name: Adam

print(NewEmp.id)
# output:
#  1

print(NewEmp.name)
# output:
# Adam

print(NewEmp.title)
# output:
# My Title


# endregion:

###################################################
# >> Inheritance and override or non-override methods using super keyword
###################################################
# region
print("#" * 50)

# If you have duplicate methods one in parent class and one in child class, and you want to call the method from the parent class we use the "super().method_name" or "parent_class.method_name(self)"


class CompanyA:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def Greet(self):
        print(f"From CompanyA Welcome {self.username}")


class UserA(CompanyA):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.username = "MR. " + username

    def Greet(self):  # this Greet method will override the Greet method from CompanyA Class
        print(f"From UserA Welcome {self.username}")

    def get_password(self):
        print(f"password is '{self.password}'")


class UserB(CompanyA):
    def __init__(self, username, password):
        self.username = "MR" + username
        CompanyA.__init__(self, username, password)

    def Greet(self):  # here we override or call the Greet() method from the CompanyA Base/Parent Class
        super().Greet()

    def get_password(self):
        print(f"password is '{self.password}'")


User1 = UserA("Adam33", "3jfek4ej65")

User1.Greet()
# output:
# From UserA Welcome MR. Adam33

User1.get_password()
# output:
# password is '3jfek4ej65'

User2 = UserB("Max45", "f788dDhnm")

User2.Greet()
# output:
# From CompanyA Welcome Max45

User2.get_password()
# output:
# password is 'f788dDhnm'

# endregion

###################################################
# >> Example
###################################################
# region

class Animal:
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")

    def bark(self):
        print("Woof!")


d = Dog()
# output:
# Animal created
# Dog created

d.whoAmI()
# output:
# dog

d.eat()
# output:
# Eating

d.bark()
# output:
# Woof!

# endregion