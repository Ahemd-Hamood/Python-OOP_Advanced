###################################################
# >> Abstract Class
###################################################
# region

# Abstract class is a class that have a common code or interface method with no implementation that all sub-classes must override and implement.
# Abstract class is assigned to a parent class that you want it to provide code that can be reuse a cross different sub-classes.
# Abstract class provide signature/interface methods for all sub-class, all sub-classes must include these abstract methods.
# Every time you create a new sub-class that inherit from an abstract parent class, all the method in the abstract class must exist/override on the sub-class.

# You can't create a new instance from an abstract class, only create a new instance from sub-class that inherit from that abstract class
# some methods inside the abstract class, have no implementation or no body which mean all derived class must use that method and provide a body to it.

from abc import ABC, abstractmethod

# >> to make our class abstract, it must inherit/derive from the ABC - Abstract Base Class
# >> to make our method abstract, we need to add the abstractmethod decorator above it.


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            print("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            print("Stream is already close.")
        self.opened = False

    @abstractmethod
    def read(self):  # with @abstractmethod decorator this method consider an abstract method with no implementation
        pass

    @abstractmethod
    def write(self):  # with @abstractmethod decorator this method consider an abstract method with no implementation
        pass

# >> Now both FileStream and NetworkStream must include or provide both read() and write() methods

class FileStream(Stream):
    def read(self):
        if self.opened:
            print("Reading data from a file")
        else:
            print("Error >> Open your stream first")

    def write(self):
        if self.opened:
            print("Writing data from a file")
        else:
            print("Error >> Open your stream first")

    def message(self):
        print("FileStream.....")


class NetworkStream(Stream):
    def read(self):
        if self.opened:
            print("Reading data from a network")
        else:
            print("Error >> Open your stream first")

    def write(self):
        if self.opened:
            print("Writing data from a network")
        else:
            print("Error >> Open your stream first")

    def message(self):
        print("NetworkStream.....")

# >> As you can see we can't create a new instance from an abstract class, because it has an abstract method

# stream = Stream()
# output:
# TypeError: Can't instantiate abstract class Stream with abstract methods read, write


class MemorySteam(Stream):
    pass
    # here you should include all Stream abstract method, otherwise this class will be consider as an abstract class
    # the moment you override and implement all abstract method here, the MemorySteam class will be a concert class
    # Which follows the interfaces or abstract methods of the Stream class signature

# >> if you don't implement an abstract methods inside the MemorySteam class, the MemorySteam class will be considered as an abstract class
# mem_stream = MemorySteam()
# output:
# TypeError: Can't instantiate abstract class MemorySteam with abstract methods read, write


file_stream = FileStream()
network_stream = NetworkStream()

file_stream.read()
# output: Error >> Open your stream first
file_stream.open()
file_stream.read()
# output: Reading data from a file
file_stream.write()
# output: Writing data from a file
file_stream.message()
# output: FileStream....

# ----------------------------------------------------

network_stream.read()
# output: Error >> Open your stream first
network_stream.open()
network_stream.read()
# output: Reading data from a network
network_stream.write()
# output: Writing data from a network
network_stream.message()
# output: NetworkStream.....


# endregion
