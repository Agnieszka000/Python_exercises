# Cyberstart Platform - Level 6, Challenge 1 - "Foreign Filesystem"

# Write a script to browse the contents of /tmp/aliendir and see if you can find a file.

from os import walk

# path to the folder
dir_path = r"/tmp/aliendir"

# list to store filenames
res = []
for (dir_path, dir_names, file_names) in walk(dir_path):
    res.extend(file_names)
print(res)