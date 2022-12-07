# python 7.py input7.txt

import sys

f = open(sys.argv[1])


system = dict()  # { path: (dirs, files_size) }
command = f.readline()[:-1]
while command:
    if command.startswith("$ cd"):
        directory = command[5:]  # Remove '$ cd'
        if directory == "..":
            current_path.pop()
        elif directory == "/":
            current_path = []
        else:
            current_path.append(directory)
        command = f.readline()[:-1]
    else:  # $ ls
        dirs = []
        files_size = 0
        command = f.readline()[:-1]
        while command and not command.startswith("$ "):
            first, second = command.split()
            if first == "dir":
                dirs.append("/".join(current_path + [second]))
            else:
                files_size += int(first)
            command = f.readline()[:-1]
        system["/".join(current_path)] = (dirs, files_size)

dir_sizes = dict()
# start by the last explored dir
for path in reversed(system.keys()):
    dirs, dir_size = system[path]
    for d in dirs:
        dir_size += dir_sizes[d]
    dir_sizes[path] = dir_size

print(sum(v for v in dir_sizes.values() if v < 100000))
