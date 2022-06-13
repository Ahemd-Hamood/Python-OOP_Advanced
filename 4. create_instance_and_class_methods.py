###################################################
# >> Define instance methods
###################################################
# region

class Class_ExampleA:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_info(self):  # create an instance method
        print(f"x:{self.x}, y:{self.y}")

    def say_hi(self, name):  # create an instance method with parameter
        print(f"Hey {name}")


instance_A = Class_ExampleA(1, 3)

print(instance_A.x)
# output: 1
print(instance_A.y)
# output: 3

# >> Access instance method using an instance object:-

instance_A.print_info()
# output:
# x:1, y:3

instance_A.say_hi("Adam")
# output:
# Hey Adam

# Class_ExampleA.print_info()
# TypeError: Class_ExampleA.print_info() missing 1 required positional argument: 'self'

Class_ExampleA.print_info(instance_A)
# output:
# x:1, y:3

# endregion

###################################################
# >> Define Class Methods - Class Level Method
###################################################
# region
print("#" * 50)

# We use the @classmethod decorator to make or convert our method to be a Class Method
# Class Method can be called by using a Class reference


class Class_ExampleB:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def start_code(self):  # create a Class Method
        print("starting...")

    @classmethod
    def print_info(self):  # create a Class Method
        print(f"x:{self.x}, y:{self.y}")


new_instance = Class_ExampleB(2, 4)

Class_ExampleB.start_code()
# output:
# starting...

new_instance.start_code()
# output:
# starting...

# Class_ExampleB.print_info()
# output:
# AttributeError: type object 'Class_ExampleB' has no attribute 'x'

# new_instance.print_info()
# output:
# AttributeError: type object 'Class_ExampleB' has no attribute 'x'

# endregion

###################################################
# >> Use Static/Class Method to create an Object instance
###################################################
# region

# We will create a class method that return an object with default constructor values, our class method will be a factory method
# Simply we will create a factory method that return a new object with default values for constructor initializer
# to create a factory method we pass 'cls' parameter into our class method, then we pass our values into the cls()
# The cls parameter is a reference to the class itself not an instance object


class My_Class:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def initialize(cls):
        print("create a new instance object . . . .", cls)
        return cls(3, 6)  # --> exactly like calling My_Class(0,0)

    def print_info(self):  # create a Class Method
        print(f"x:{self.x}, y:{self.y}")

# At run time when we call the class method initialize() python interpreter will automatically pass a reference to the My_Class class object


instance_1 = My_Class.initialize()
# output:
# create a new instance object . . . . <class '__main__.My_Class'>

instance_1.print_info()
# output:
# x:3, y:6

instance_2 = My_Class.initialize()
# output:
# create a new instance object . . . . <class '__main__.My_Class'>

instance_2.print_info()
# output:
# x:3, y:6

# endregion
