###################################################
# >> Extending Build-in Types
###################################################
# region

# We can use inheritance with a build-in type in python. By creating a class that inherit from a build-in type.

# >> We will a class called "Text" that inherit from the build-in string class, which means that our Text class has all the features of python strings.
# >> We can add an additional feature like methods into our Text class.


class Text(str):
    def duplicate(self):
        return self + " " + self

    def add_title_name(self):
        return "Mr. " + self


obj1 = Text("Python")

# >> all string features also are available inside the Text class

print(obj1.lower())
# output:
# python

print(obj1.duplicate())
# output:
# Python Python

user1 = Text("Adam")

print(user1.add_title_name())
# output:
# Mr. Adam

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>> Override some Build-in type methods >>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# also we can define a class that extend/inherit from the list class.
# we are going to override the append class, do something with it then call the original append method from the list class using the super() keyword


class TrackableList(list):
    def append(self, obj):
        print("append called.....")
        super().append(obj)  # called the original append from the list class

    def pop(self):
        print("pop called.....")
        super().pop()  # called the original pop() method from the list class


new_list = TrackableList()

new_list.append("1")  # output: append called.....
new_list.append("2")  # output: append called.....
new_list.append("3")  # output: append called.....

print(new_list)
# output:
# ['1', '2', '3']

new_list.pop()  # output: pop called.....
new_list.pop()  # output: pop called.....

print(new_list)
# output:
# ['1']

new_list.pop()  # output: pop called.....

print(new_list)
# output:
# []

# endregion
