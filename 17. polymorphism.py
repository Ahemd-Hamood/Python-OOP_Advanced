from abc import ABC, abstractmethod
###################################################
# >> Polymorphism
###################################################
# region

# >> Here the UIControl have two interfaces that all derivative/sub-classes will follow


class UIControl(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def remove(self):
        pass

# >> The TextBox must implement both render() and remove() methods


class TextBox(UIControl):
    def render(self):
        print("Render TextBox...")

    def remove(self):
        print("Remove TextBox...")

# >> The DropDownList must implement both render() and remove() methods


class DropDownList(UIControl):
    def render(self):
        print("Render DropDownList...")

    def remove(self):
        print("Remove DropDownList...")

# >> The CheckBox must implement both render() and remove() methods


class CheckBox(UIControl):
    def render(self):
        print("Render CheckBox...")

    def remove(self):
        print("Remove CheckBox...")

# >> Here we define a method that takes a UIControl object to call the render() and remove() methods


def render(control):
    control.render()


def remove(control):
    control.remove()

# >> Now we will create three object instances from TextBox, DropDownList CheckBox classes/objects
# >> and pass each instance into the render() and remove() methods that expect an UIControl object at run time
# >> Both render() and remove() methods are expecting a derived class from the UIControl we call this "Polymorphism" Many-Forms.


tb = TextBox()
ddl = DropDownList()
cb = CheckBox()

# >> In the following we will pass any of the UIControl object derivatives

# >> passing instance tb object will call the render, remove method from the TextBox object
render(tb)  # output: Render TextBox...
remove(tb)  # output: Remove TextBox...
print(isinstance(tb, UIControl))  # output: True

# >> passing instance ddl object will call the render, remove method from the TextBox object
render(ddl)  # output: Render DropDownList...
remove(ddl)  # output: Remove DropDownList...
print(isinstance(ddl, UIControl))  # output: True

# >> passing instance cb object will call the render, remove method from the TextBox object
render(cb)  # output: Render CheckBox...
remove(cb)  # output: Remove CheckBox...
print(isinstance(cb, UIControl))  # output: True

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# "Polymorphism" defines methods in the child class that have the same name as the methods in the parent class.
# In inheritance, the child class inherits the methods from the parent class.
# Also, it is possible to modify a method in a child class that it has inherited from the parent class.

# >> The following methods will iterate thru each control object.


def render2(controls):
    for control in controls:
        control.render()


def remove2(controls):
    for control in controls:
        control.remove()


render2([tb, ddl, cb])
# output:
# Render TextBox...
# Render DropDownList...
# Render CheckBox...

remove2([tb, ddl, cb])
# output:
# Remove TextBox...
# Remove DropDownList...
# Remove CheckBox...

# endregion

###################################################
# >> Achieving Polymorphism behavior
###################################################
# region

# >> To Achieve Polymorphism behavior :-

# 1. we start by defining a Base/abstract Class, and within this class we define common methods with no implementation.
# 2. then we create a children classes that inherit/derivative from that Base Class.
# 3. and each child class implement and define the base class methods
# 4. after that we create a multi-form method that accept an abstract class parameter control object, so we can pass any derivative object type to it.
# 5. depending on the type of the control object that we are working with at the runtime, our multi-form method takes a different form.
# 6. now we can pass any of the derivative classes object into the multi-form method parameter to call any method of the derived class

# endregion

###################################################
# >> Achieving Polymorphism behavior without using abstract - duck typing
###################################################
# region
print("#" * 50)

# >> we can still achieve Polymorphism without using an abstract class.
# >> Only you need to make sure that every class has a similar method to call.
# >> still using an abstract class as a common interface a cross all child class, so to make sure all derivative classes has a common/similar method


class TextBox():
    def render(self):
        print("Render TextBox...")

    def remove(self):
        print("Remove TextBox...")


class DropDownList():
    def render(self):
        print("Render DropDownList...")

    def remove(self):
        print("Remove DropDownList...")


tb = TextBox()
ddl = DropDownList()

# >> here our render and remove method will call the object.render() method base on which object we pass to it as long the render and remove method is available


def render(controls):
    for control in controls:
        control.render()


def remove(controls):
    for control in controls:
        control.remove()


# >> as long our parameter is iterable, our code will work
render([tb, ddl])
# output:
# Render TextBox...
# Render DropDownList...

remove([tb, ddl])
# output:
# Remove TextBox...
# Remove DropDownList...


# endregion

###################################################
# >> Polymorphism Example 1
###################################################
# region

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Woof!'


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name+' says Meow!'


myDog = Dog('Niko')
myCat = Cat('Felix')

print(myDog.speak())
# output:
# Niko says Woof!

print(myCat.speak())
# output:
# Felix says Meow!

# >> Demonstrate polymorphism :-

for pet in [myDog, myCat]:
    print(pet.speak())

# output:
# Niko says Woof!
# Felix says Meow!

# >> Call function with different pet object :-


def pet_speak(pet):
    print(pet.speak())


pet_speak(myDog)
# output:
# Niko says Woof!

pet_speak(myCat)
# output:
# Felix says Meow!

# endregion

###################################################
# >> Polymorphism Example 2
###################################################
# region

class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def speak(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return self.name + ' says Woof!'


class Cat(Animal):
    def speak(self):
        return self.name + ' says Meow!'


fido = Dog('Fido')
dodo = Cat('dodo')

print(fido.speak())
# output:
# Fido says Woof!

print(dodo.speak())
# output:
# dodo says Meow!

# endregion
