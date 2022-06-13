###################################################################
# 1. >> Error Examples
###################################################################
# region

# We encounter errors because of programing mistake, or bad data that we get from the user or resources not being available.
# When an application crashes, the programmer responsibility is to a void these error, or display a proper message error when they can't be handled.
# for example, user trying to access non-existed file, then we show an error message "this file does not exist"

# Exception is a kind of error that terminates the execution of a program. When an error happen in certain line
# Python terminate the execution which prevent the next lines of code from executing.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 1 - Programmer Error - Index out of range
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

numbers = [1, 2, 3]

print(numbers[1])
# output:
# 2

# >> But if we try to print and access an index not available, then we get an error called "IndexError"
# print(numbers[3])
# output:
# IndexError: list index out of range


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example 2 - Error while getting an user input - Index out of range
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# the input method return a string, then we convert it into integer. User will enter invalid.

if False:
    user_age = int(input("Age: "))

# > Age: twenty two  // here python interpreter will convert 'twenty two' into an integer, this will lead us to an error
# > ValueError: invalid literal for int() with base 10: 'd'


# endregion

###################################################################
# 2. >> Handling Exceptions with try-except-else
###################################################################
# region

# To handle exceptions we need to put our statement that may cause the error inside a "try:" block
# Then we add an "except:" clause that we will handle all kind of type errors inside it

# Inside the try block python will execute every statement in this block. If any of these statement throws an exception,
# the code in the except clause will be executed only if one of the statements above will cause an error exception.

# try:
#   statement1 ...
#   statement2 ...
#   statement3 ...
# except <error_type_1> :
#   print("an error message")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# A. Handling all type of error with try: and except: only
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

if False:
    try:
        user_age = int(input("Age: "))
        print(f"You age is {user_age}")
    except:  # here we will catch any/all types of error
        print("Error >> An error happened")

# > Age: 32
# > You age is 32

# > Age: abc (entering invalid non-numeric)
# > Error >> An error happened

# >> Line 60 won't run if an error happen

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# B. Handling a specific type of error with try and except <error_type>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# We know when a user enters a non-numeric value, we are gonna get ValueError Type.
# So we can specify which type of error we're gonna handle, just specify your expected error type after the except clause
# like this : except ValueError

# >> Example 1 :

if False:
    try:
        user_age = int(input("Age: "))
        print(f"You age is {user_age}")
    except ValueError:  # here we will only catch ValueError
        print("You did not enter a valid age.")

print("Execution Continues ....")

# output:
# > Age: 22
# > You age is 22
# > Execution Continues ....

# > Age: abc (entering invalid non-numeric)
# > Error >> An error happened
# > Execution Continues ....

# >> Example 2 :

numbers = [1, 2, 3]

if False:
    try:
        print(numbers[3])
    except IndexError:
        print("Index is out of range")

# output:
# Index is out of range

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# C. Using an optional else clause
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# The else clause block will be executed if no exception is thrown in the code that we have inside the try block.
# the else clause will only be executed if we don't have any exceptions.

if False:
    try:
        user_age = int(input("Age: "))
        print(f"You age is {user_age}")
    except ValueError:  # here we will only catch ValueError
        print("You did not enter a valid age.")
    else:
        print("No Error happened....")

# output 1:
# > Age: 22
# > You age is 22
# > No Error happened....

# output 2:
# Age: ff
# You did not enter a valid age.


# endregion

###################################################################
# 3. >> Get exception error details with except <Error_Type> as variable
###################################################################
# region

# we can optionally define a variable that will include the details about the exception, mostly the error message and sometime additional arguments
# we define our detail variable after the except like this:
# except <Error_Type> as ex: --> it can be ex, error, err

if False:
    try:
        user_age = int(input("Age: "))
        print(f"You age is {user_age}")
    except ValueError as err:  # here we will only catch ValueError
        print("You did not enter a valid age.")
        print("Error details:", err)
        print(type(err))
    else:
        print("No Error happened....")

# output:
# > Age: abc
# > You did not enter a valid age.
# > Error details: invalid literal for int() with base 10: 'ef'
# > <class 'ValueError'>

# endregion

###################################################################
# 4. >> Handling Different Exception
###################################################################
# region

if False:
    try:
        user_age = int(input("Enter Age: "))
        xfactor = 10 / user_age
    except ValueError:
        print("Age is invalid...")
    else:
        print(f"Your Age is {user_age}")

# output:
# > Enter Age: 22
# > Your Age is 22

# output:
# > Enter Age: 0
# > ZeroDivisionError: division by zero

# >> As you see above we got a different kind of exception error called "ZeroDivisionError" - it happened because we divide a number by zero.
# >> because we don't have a matching exception in except clause for that kind of exception error. In our code above we're only handling "ValueError" exceptions

# >> To solve this problem we can apply the following :-

# ***********************************
# A. Add a second except clause
# ***********************************

if False:
    try:
        user_age = int(input("Enter Age: "))
        xfactor = 10 / user_age
    except ValueError:
        print("Age is invalid...")
    except ZeroDivisionError:
        print("Age can not be 0.")
    else:
        print(f"Your Age is {user_age}")

# output:
# > Enter Age: 0
# > Age can not be 0.

# ***********************************
# B. Single except clause with multiple types of exception
# ***********************************

# >> We can have in front of the except clause we can specify multiple types of exceptions.
# >> If the exception that is thrown matches any of those exceptions then the code in the except block will be executed.
# >> to specify multiple types of exception we just add our types after the except clause around parenthesis separated by comma like this :
# except (type_error_1, type_error_2, type_error_3, .....):

if False:
    try:
        user_age = int(input("Enter Age: "))
        xfactor = 10 / user_age
    except (ValueError, ZeroDivisionError):
        print("You have enter an invalid Age...")
    else:
        print(f"Your Age is {user_age}")

# output 1:
# > Enter Age: abc
# > You have enter an invalid Age...

# output 2:
# > Enter Age: 0
# > You have enter an invalid Age...

# >> When python execute our code statement inside the try block, if any of the statements throws an exception error that matches one of the except clause.
# >> Then the except clause will be executed and it will ignore any other except clause that you may have next

numbers = [1, 2, 3]


def some_fun(condition):
    if False:
        try:
            user_age = int(input("Enter Age: "))
            xfactor = 10 / user_age
            if condition:
                print(numbers[3])
        except (ValueError, ZeroDivisionError) as ex:
            print("You have enter an invalid Age...")
            print("Error:", ex)
        except:
            print("Unknown Error happened .....")
        else:
            print(f"Your Age is {user_age}")


some_fun(False)

# output 1:
# > Enter Age: 22
# > Your Age is 22

# output 2:
# > Enter Age: abc
# > You have enter an invalid Age...
# > Error: invalid literal for int() with base 10: 'abc'

# output 3:
# > Enter Age: 0
# > You have enter an invalid Age...
# > Error: division by zero

some_fun(True)

# output:
# > Enter Age: 3
# > Unknown Error happened .....

# endregion

# ********************************************************************************************
# ********************************************************************************************
# ********************************************************************************************

###################################################################
# 5. >> Cleaning up external resources using the finally clause
###################################################################
# region

# >> There are some situations that we need to work with external resources like files, network connections, databases ans so on.
# >> These resources after we're done using them, we need to release them.
# >> For Example, when we open a file we should always close it after we are done. otherwise another process/program may not able to open that file.

if False:
    try:
        file = open("my_file.txt")
        print("reading file....")
        user_age = int(input("Enter Age: "))
        xfactor = 10 / user_age
    except (ValueError, ZeroDivisionError):
        print("You have enter an invalid Age...")
        file.close()
    else:
        print("No Exception Error")
        file.close()

# >> here we are duplicating our "file.close()" line code, close the file if :-
# 1. an exception error happen
# 2. or if no exception error happen

# >> We can simply use the "final:" clause at the end. the finally clause is always executed wether we have a exception or not.
# >> We use the finally clause to release external resources. So it's the perfect place to close file, database connections, network connections and so on.
# >> we can simply say we use the final clause to release external resources manually mean you have to do it by yourself

if False:
    try:
        file = open("my_file.txt")
        print("reading file....")
        user_age = int(input("Enter Age: "))
        xfactor = 10 / user_age
    except (ValueError, ZeroDivisionError):
        print("You have enter an invalid Age...")
    except (FileNotFoundError):
        print("File does not exist...")
    else:
        print("No Exception Error")
    finally:
        file.close()
        print("file closed....")

# output 1:
# reading file....
# > Enter Age: 33
# No Exception Error
# file closed....

# output 2:
# reading file....
# >> Enter Age: abc
# You have enter an invalid Age...
# file closed....

# endregion

###################################################################
# 6. >> Cleaning up external resources using the with statement
###################################################################
# region

# >> We have another way to release external resources, with out the need to use the finally clause.
# >> This way only works with certain objects.

# >> We will use the with statement to open/access a file, python will automatically call file.close() wether we have finally clause or not.
# >> We can simply say the with statement is used to automatically release external resources

if False:
    # - Before - read file with the read() method, and close the file with the close() method.
    file = open("my_file.txt")
    print("Open File")
    print(file.read())
    print("Close File")
    file.close()

if False:
    # After - file store the return value of file -- and our file will be closed automatically after reading it.
    with open("my_file.txt") as file:
        print("Open File")
        print(file.read())
        print("Close File")

# >> We better add our file reading inside a try-except in case of some error may happen

if False:
    try:
        with open("my_file.txt") as file:
            print("Open File")
            print(file.read())
            print("Close File")
        user_age = int(input("Enter Age: "))
        xfactor = 10 / user_age
    except (ValueError, ZeroDivisionError):
        print("You have enter an invalid Age...")
    except (FileNotFoundError):
        print("File does not exist...")
    else:
        print("No Exception Error")

# output:
# > Open File
# > some text
# > Close File
# > Enter Age: 33
# > No Exception Error

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# How does with statement works with the file object :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# If you check the members of the file object, you gonna find two magic method that start with double underscore :

if False:
    with open("my_file.txt") as file:
        file.__enter__()
        file.__exit__()

# The __enter__ and __exit__ methods, if any object has these two methods, we can say that object supports "context management protocol".
# We can use that object with the "with" statement. Python will automatically call the exit method which will release external resources.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Using multiple external resources :-
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# with source_1_call() as src1, source_1_call() as src2, source_1_call() as src3:
  # here we deal with src1, src2 and src3

if False:
    try:
        with open("my_file.txt") as file, open("another_file.txt") as target:
            print("Open my_file.txt")
            print(file.read())
            print("Open another_file.txt")
            print(target.read())
            print("both files are closed...")
    except (FileNotFoundError):
        print("File does not exist...")
    else:
        print("No Exception Error")

# output:
# File does not exist...

# endregion

###################################################################
# 7. >> Raise an Exception
###################################################################
# region

# Before we learned how to handle exception errors, now will learn how to raise or throw exceptions within ur code.
# To an raise an exception, we use the "raise" statement, then we specify the type of our exception


def get_date_of_birth(age):
    if type(age) != int:  # or --> not isinstance(age, int)
        raise ValueError("Age must be a number")
    if age <= 0:
        raise ZeroDivisionError("Age can not be 0 or less")
    print(f"Your data of birth is in {2020 - age}")


if False:
    get_date_of_birth(22)
    # output:
    # Your data of birth is in 1998

    get_date_of_birth(0)
    # output:
    # ZeroDivisionError: Age can not be 0 or less

    try:
        get_date_of_birth("222")
    except ValueError as err:
        print(err)
    # output:
    # Age must be a number

    try:
        get_date_of_birth(-1)
    except ValueError as err:
        print(err)
    # output:
    # Age can not be 0 or less

# endregion

###################################################################
# 8. >> Python build-in exceptions
###################################################################
# region

# ArithmeticError :-	Raised when an error occurs in numeric calculations
# AssertionError :-	Raised when an assert statement fails
# AttributeError :-	Raised when attribute reference or assignment fails
# Exception :-	Base class for all exceptions
# EOFError :-	Raised when the input() method hits an "end of file" condition (EOF)
# FloatingPointError :-	Raised when a floating point calculation fails
# GeneratorExit :-	Raised when a generator is closed (with the close() method)
# ImportError :-	Raised when an imported module does not exist
# IndentationError :-	Raised when indendation is not correct
# IndexError :-	Raised when an index of a sequence does not exist
# KeyError :-	Raised when a key does not exist in a dictionary
# KeyboardInterrupt :-	Raised when the user presses Ctrl+c, Ctrl+z or Delete
# LookupError :-	Raised when errors raised cant be found
# MemoryError :-	Raised when a program runs out of memory
# NameError :-	Raised when a variable does not exist
# NotImplementedError :-	Raised when an abstract method requires an inherited class to override the method
# OSError :-	Raised when a system related operation causes an error
# OverflowError :-	Raised when the result of a numeric calculation is too large
# ReferenceError :-	Raised when a weak reference object does not exist
# RuntimeError :-	Raised when an error occurs that do not belong to any specific expections
# StopIteration :-	Raised when the next() method of an iterator has no further values
# SyntaxError :-	Raised when a syntax error occurs
# TabError :-	Raised when indentation consists of tabs or spaces
# SystemError :-	Raised when a system error occurs
# SystemExit :-	Raised when the sys.exit() function is called
# TypeError :-	Raised when two different types are combined
# UnboundLocalError :-	Raised when a local variable is referenced before assignment
# UnicodeError :-	Raised when a unicode problem occurs
# UnicodeEncodeError :-	Raised when a unicode encoding problem occurs
# UnicodeDecodeError :-	Raised when a unicode decoding problem occurs
# UnicodeTranslateError :-	Raised when a unicode translation problem occurs
# ValueError :-	Raised when there is a wrong value in a specified data type
# ZeroDivisionError :-	Raised when the second operator in a division is zero

# endregion

###################################################################
# 9. >> Define a Custom Exception
###################################################################
# region

# >> We can define custom exceptions by creating a new class, and our class must derive/inherit either directly or in-directly from the built-in "Exception" class.
# >> Most of the built-in exceptions are also derived from the "Exception" class.

class MyCustomError(Exception):
    pass

# >> As you see above we have create a custom user-define exception called MyCustomError which inherit from from the Exception class.
# >> This new exception, like other exceptions, can be raised using the "raise" statement with an optional error message.


if False:
    raise MyCustomError("An Error occurred.")

# output:
# __main__.MyCustomError: An Error occurred.


# >> Example:-

class InvalidOperationError(Exception):
    pass


class UsernameTooShort(Exception):
    pass


if False:
    user_input = input("Enter a number: ")
    try:
        if user_input == "1":
            raise MyCustomError("An Error Occurred.")
        if user_input == "2":
            raise InvalidOperationError
        if user_input == "3":
            raise UsernameTooShort
    except MyCustomError:
        print("Error happened...")
    except InvalidOperationError:
        print("Invalid Operation Error")
    except UsernameTooShort:
        print("Username is too short")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example: User-Defined Exception
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# define Python user-defined exceptions


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
if False:
    while True:
        try:
            i_num = int(input("Enter a number: "))
            if i_num < number:
                raise ValueTooSmallError
            elif i_num > number:
                raise ValueTooLargeError
            break
        except ValueTooSmallError:
            print("This value is too small, try again!")
            print()
        except ValueTooLargeError:
            print("This value is too large, try again!")
            print()

    print("Congratulations! You guessed it correctly.")


# Output:

# > Enter a number: 12
# This value is too large, try again!

# > Enter a number: 0
# This value is too small, try again!

# > Enter a number: 8
# This value is too small, try again!

# > Enter a number: 10
# Congratulations! You guessed it correctly.

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >> Example: Customizing Exception Classes
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):  # here we override the string magic method from the Exception Class
        return f'{self.salary} ---> {self.message}'


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)


# Output:

# > Enter salary amount: 3000
# __main__.SalaryNotInRangeError: 3000 ---> Salary is not in (5000, 15000) range

# > Enter salary amount: 12000
#


# endregion
