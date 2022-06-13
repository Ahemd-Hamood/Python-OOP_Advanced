# >> Create a custom exception

class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already close.")
        self.opened = False


class FileStream(Stream):
    def read(self):
        if self.opened:
            print("Reading data from a file")
        else:
            print("Error >> Open your stream first")


class NetworkStream(Stream):
    def read(self):
        if self.opened:
            print("Reading data from a network")
        else:
            print("Error >> Open your stream first")


file_1 = FileStream()

file_1.read()
# output: Error >> Open your stream first
file_1.open()
file_1.read()
# output: Reading data from a file
file_1.close()

file_2 = NetworkStream()

file_2.open()
file_2.read()
# output: Reading data from a network
file_2.close()
