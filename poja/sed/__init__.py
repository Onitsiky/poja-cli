import os
from fnmatch import fnmatch


def find_replace(directory, find, replace, exclude_pattern):
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in [f for f in files if not fnmatch(f, exclude_pattern)]:
            filepath = os.path.join(path, filename)
            with open(filepath, errors="ignore") as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)


def remove_line_by_keyword(filename, keyword):
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            if keyword not in line:
                file.write(line)
