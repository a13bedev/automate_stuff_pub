"""
This program walks through a folder tree and searches for files with size
greater or equal 100MB and prints files with their absolute path to the screen.
"""

import os

path = input("Enter a path to a folder.\n")
# Using size of subfolders is pretty good idea since it lets to skip
# the ones with size less than 100
result = {}  # Resulting dictionary with absolute path as a key and size as a value
for curr_folder, subfolders, file_names in os.walk(path):
    pass
