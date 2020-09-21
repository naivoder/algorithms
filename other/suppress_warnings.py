"""
this file is a simple demo of how to selectively ignore exceptions a.k.a. context manager
this implementation will delete a file only if it is present, ignoring the exception if it is not

"""
from os import remove
from contextlib import suppress


def delete_if_present(file):
    with suppress(FileNotFoundError):
        remove(file)
        print('File Deleted!')
        return 1
    print('File Does Not Exist!')


if __name__ == "__main__":
    fake_file = 'this_file_doesnt_exist.txt'
    delete_if_present(fake_file)
