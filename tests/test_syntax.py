import os
import py_compile


def recurse(directory):
    for filename in os.listdir(directory):
        full_path = os.path.join(directory, filename)
        if full_path.endswith('.py'):
            py_compile.compile(full_path, doraise=True)
        if os.path.isdir(full_path):
            recurse(full_path)


def test_syntax():
    recurse(os.getcwd())
