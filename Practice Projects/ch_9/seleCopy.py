"""
This program walks through a folder tree and
searches for files with certain file extension (such as .pdf or .jpg) and
copies this files from a whatever location into a new folder.
Program will REWRITE files if they have the same name.
"""
import os
import shutil

# Request for a path to search in.
path = input("Enter a path to a folder to copy from.\n")
while True:
    if not os.path.exists(path):
        print('Path is incorrect')
        path = input("Enter a path to a folder to copy from.\n")
    else:
        print('Success. Path to copy from assigned.')
        break

# Ask for file extensions.
file_extensions = set(input("Enter extension(s) without dot ('.') "
                            "use white space to separate multiple.\n").split())

# Ask location of a new folder.
new_folder_path = input("Enter a path to a folder to copy into.\n")
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)
    print('Path %s was created' % new_folder_path)

# Walk trough a folder tree and check if there are sought-for extensions.
for curr_folder, subfolders, file_names in os.walk(path):
    for file_name in file_names:
        tail = file_name.split('.')[-1]  # Extension
        if tail in file_extensions:
            shutil.copy(curr_folder + '\\' + file_name, new_folder_path)
print("It's done.")
