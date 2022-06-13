###################################################
# >> Data Classes using the namedtuple method
###################################################
# region

# >> Data classes mean when a class don't have any methods, but it only has data or attributes that we initialize while calling the class.

from collections import namedtuple


class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age


user1 = UserInfo("Adam", 44)
user2 = UserInfo("Sam", 23)

print(user1.name)  # output: Adam
print(user1.age)  # output: 44

print(user2.name)  # output: Sam
print(user2.age)  # output: 44


user3 = UserInfo("David", 22)
user4 = UserInfo("David", 22)

# >> If we compare these two objects that has similar attribute values, we will get 'False' .

print(user3 == user4)
# output:
# False

# >> Because these two object user3 and user4 are stored in different locations in memory.
# >> If we have two objects referencing the same object memory then we can consider them equal

# >> to print the address of memory location of each object we use the id() build-in method

print(id(user3))  # output: 2251258920576
print(id(user4))  # output: 2251258920480

# >> As you can see these objects are in two different location in memory
# >> to solve the issue with comparing two UserInfo objects, we need to do one of the following solutions :-

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Solution 1 - use the __eq__() magic method
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


class UserInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other_obj):
        return self.name == other_obj.name and self.age == other_obj.age


user1 = UserInfo("David", 22)
user2 = UserInfo("David", 22)

# >> As you see we get True, by using the __eq__ magic method
print(user1 == user2)
# output:
# True

# >> still both objects are referencing to different location memory address

print(id(user1))  # output: 1419973557600
print(id(user2))  # output: 1419973558176


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Solution 2 - use the namedtuple() function from the collection module
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# >> If you are dealing we classes that have no behavior, no methods, they only have data, we can use a 'named tuple' instead.
# >> the namedtuple the only benefit is that we don't have to explicitly implement a magic method to compare two objects
# >> from the collection module we import the namedtuple function.

# from collections import namedtuple

# In our namedtuple function : first argument we can specify the name of new type that we want to create so we are going to call it "UserInfo"
# In our namedtuple function : second argument we pass an array or list of our field names or attribute names [att1, att2, att3, ...]
# namedtuple return a named tuple that we can store


User_Info = namedtuple("UserInfo", ["name", "age"])

user1 = User_Info("Adam", 22)

print(user1.name)  # output: Adam
print(user1.age)  # output: 22

# >> Our named tuples are immutable which means once we create them, we can't modify them, we can not mutate them.
# >> If you want to modify your named tuple then you need to create a new namedtuple object

# user1.name = "Frank"
# output:
# AttributeError: can't set attribute

# >> We use key argument to make our code more clear
user2 = User_Info(name="Adam", age=22)

print(user2.name)  # output: Adam
print(user2.age)  # output: 22

# >> If we compare user1 and user2 we will get true, both objects are equal without the need of implementing the __eq__() magic method

print(user1 == user2)
# output:
# True

# >> yes they are in different location, but still better than implementing the __eq__ magic method, using namedtuple is short and readable

print(id(user1))  # output: 2107264730688
print(id(user2))  # output: 2107264948800


# endregion