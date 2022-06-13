###################################################
# >> Problem 1 - Access Class Attribute Directly
###################################################
# region

class Class_Example:
    def __init__(self):
        self.users = ["user1", "user2", "user3"]

    def add_user(self, user):
        self.users.append(user)

    def get_user(self):
        return self.users

    def get_user_by_index(self, index):
        if index < len(self.users) - 1:
            return self.users[index]
        else:
            return "Index Error"


sys_1 = Class_Example()

sys_1.add_user("user4")
sys_1.add_user("user5")

print(sys_1.get_user())

# output:
# ['user1', 'user2', 'user3', 'user4', 'user5']

print(sys_1.get_user_by_index(1))  # output: user2
print(sys_1.get_user_by_index(3))  # output: user4
print(sys_1.get_user_by_index(5))  # output: Index Error

# >> As you know can access the users list directly, using your class instance, and get the same result like get_user()

print(sys_1.users)
# output:
# ['user1', 'user2', 'user3', 'user4', 'user5']

print(sys_1.users[1])  # output: user2
print(sys_1.users[3])  # output: user4

# >> If you try to access invalid user index, your program is going to crush with "list index out of range" Error

# print(sys_1.users[5])
# output:
# IndexError: list index out of range

# >> As you see the problem in our class is this class it gives us access to the users list that we use to store our users
# >> We want only to interact with the users list thru get_user() and get_user_by_index() methods only, so
# >> We need to prevent or hide the users attribute from the outside so nobody can access it or make it in-accessible

# endregion

###################################################
# >> Private Members - Private Attribute and Method
###################################################
# region

# To make our attribute private or in-accessible from the outside, we need to prefix it with two underline like this "__"
# so all users list attributes will have double underscore at the beginning which makes it private or in-accessible
# We will add another method called some_message() and make it private or in-accessible, only its accessible within the class itself


class Private_Attribute_Example:
    def __init__(self):
        self.__users = ["user1", "user2", "user3"]

    def add_user(self, user):
        self.__users.append(user)

    def get_user(self):
        self.__some_message()
        return self.__users

    def get_user_by_index(self, index):
        if index < len(self.__users) - 1:
            return self.__users[index]
        else:
            return "Index Error"

    def __some_message(self):  # this method is consider private with double underscore prefix
        print("Welcome")


instance_1 = Private_Attribute_Example()

instance_1.add_user("user4")
instance_1.add_user("user5")

print(instance_1.get_user())
# output:
# Welcome
# ['user1', 'user2', 'user3', 'user4', 'user5']

# >> You cant access __some_message() because it's private

# instance_1.__some_message()
# output:
# AttributeError: 'Private_Attribute_Example' object has no attribute '__some_message'

# >> You cant get users because it's private

# print(instance_1.__users)
# output:
# AttributeError: 'Private_Attribute_Example' object has no attribute '__users'

# >> You cant access users because it's private

# print(instance_1.__users[1])
# output: AttributeError: 'Private_Attribute_Example' object has no attribute '__users'
# print(instance_1.__users[3])
# output: AttributeError: 'Private_Attribute_Example' object has no attribute '__users'

# endregion

###################################################
# >> Access Private Members - not recommended
###################################################
# region

# You still can access private members from the outside, yes they are accessible but it's not convenient or necessary to access them
# private member in python is not meant for security, it only means warning or alert to someone who is using this class,
# it just to let anyone be aware that this class has private members, so don't touch them because they are private
# In python we don't have the real concept of private like other languages, it just to prevent accidental access of these private members
# If you still want to access them for no reason, let me show you how

# Every class/object has a property called __dic__, its dictionary that holds or stores all the attributes only in this class

class ClassA:
    def __init__(self):
        self.__attA = "value1"
        self.__attB = "value2"

    def __some_message(self):
        print("Welcome")


instance_A = ClassA()

print(instance_A.__dict__)
# {
#  '_ClassA__attA': 'value1',
#  '_ClassA__attB': 'value2'
# }

# >> If you notice, python interpreter store users attribute and it automatically renames or prefix it with the name of it's class
# like this :- _<classname>__<attributename>
# this means we can still access these attributes by their new name directly using our class instance like this :-

print(instance_A._ClassA__attA)
# output:
# value1
print(instance_A._ClassA__attB)
# output:
# value2

# endregion
