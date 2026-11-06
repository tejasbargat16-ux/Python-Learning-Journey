import os
from contextlib import contextmanager


@contextmanager
def change_dir(path):
    old_path = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old_path)


print("Before:", os.getcwd())

with change_dir(".."):
    print("Inside:", os.getcwd())

print("After:", os.getcwd())
