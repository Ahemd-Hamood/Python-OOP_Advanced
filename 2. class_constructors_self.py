# We want to supply initial values while creating new object from our class, to achieve this we apply constructor.
# constructor is a special method that is called when we create a new object from class.
# to create a constructor we use a special method called __init__() which is executed when we create a new object class

class Info_User:
    def __init__(self, name, age, gender):
        self.name = name  # here we create/add a new variable/attribute to self:Info_User called "name" and assign name parameter value to it
        self.age = age  # here we create/add a new variable/attribute to self:Info_User called "age" and assign age parameter value to it
        self.sex = gender  # here we create/add a new variable/attribute to self:Info_User called "sex" and assign gender parameter value to it

    def print_user_info(self):
        # Below we use our variable/attribute within self:Info_User
        print(
            f"name: {self.name}, gender is {self.sex}, age is {self.age} years old")

    def other_function(self):
        self.print_user_info()

# The __init__() method is like any other method we must provide at least one parameter which is "self" by convention
# In __init__(self) we can provide an additional parameters that we can use to initialize value for the class object
# The self keyword similar to this. is a reference to the current object class, that we will use to create variable attributes/properties
# We can use self object instance reference to access class member like attributes and functions

# >> To create an instance attribute variables we add them into self object, which refer to the current object - self has the following attribute variables :-
# - self.name = name
# - self.age = age
# - self.sex = gender


# >> user1, user2 each has a reference to Info_User object class as it's own copy, which only it's data belong to it.
# user1 has it's own reference copy to Info_User class object - user1:Info_User instance reference belongs to adam info only
user1 = Info_User("Adam", 12, "Male")
# user2 has it's own reference copy to Info_User class object - user2:Info_User instance reference belongs to Sally info only
user2 = Info_User("Sally", 32, "Female")
# user3 has it's own reference copy to Info_User class object - user3:Info_User instance reference belongs to David info only
user3 = Info_User("David", 22, "Male")

user1.print_user_info()
# output:
# name: Adam, gender is Male, age is 12 years old

print(f"name: {user1.name}, gender: {user1.sex}, age: {user1.age}")
# output:
# name: Adam, gender: Male, age: 12
# ____________________________________________

user2.print_user_info()
# output:
# name: Sally, gender is Female, age is 32 years old

print(f"name: {user2.name}, gender: {user2.sex}, age: {user2.age}")
# output:
# name: Sally, gender: Female, age: 32
# ____________________________________________

user3.print_user_info()
# output:
# name: David, gender is Male, age is 22 years old

print(f"name: {user3.name}, gender: {user3.sex}, age: {user3.age}")
# output:
# name: David, gender: Male, age: 22

# >> We can access other methods inside a method
user1.other_function()
# output:
# name: Adam, gender is Male, age is 12 years old  