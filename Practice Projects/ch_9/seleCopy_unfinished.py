"""
This is unfinished version of seleCopy.py.
Intention was to let program create new names instead of rewrite file with the same name.
Failed miserably.
"""
import shutil
import os

# Request for a path to search in.
path = input("Enter a path to a folder to copy from.\n")

# Ask for file extensions.
file_extensions = set(input("Enter extension(s) without dot ('.') "
                            "use white space to separate multiple\n").split())

# Ask location of a new folder.
new_folder_path = input("Enter a path to a folder to copy into.\n")

# Copy all files with requested extensions from a folder tree to a new one.


new_fold_file_list = [i for i in os.listdir(new_folder_path)
                      if os.path.isfile(os.path.join(new_folder_path, i))]  # Form a list with full file names if
# there are files in a new folder
storage = {}  # New folder file names storage
for name in new_fold_file_list:
    head = '.'.join(name.split('.')[:-1])
    tail = name.split('.')[-1]
    if tail in file_extensions:  # Check if there are sought-for extensions in a list.
        storage[head] = 1

# print('storage: %s' % storage)
# print('new_fold: %s' % new_fold_file_list)
# print(file_extensions)

# Walk trough a folder tree
for curr_folder, subfolders, file_names in os.walk(path):
    #print(curr_folder)
    #for i in file_names:
    #    print(i)
    for file_name in file_names:
        head = '.'.join(file_name.split('.')[:-1])  # File name without '.' and extension +++
        tail = file_name.split('.')[-1]  # Extension +++
        #print('head: ', head, 'tail: ', tail)
        # TODO fix logic of assigning new names cause
        # Problem is that if files in new folder have the same names especially
        # like:
        # new folder = [ba.txt, ba_(1).txt, ba_(1)_(1).txt .... etc.]
        # start folder = [ba.txt]
        # and the patter is adding _(number = value from storage)
        # things become messy

    #     if tail in file_extensions:
    #         if storage.get(head):  # if file has the same name as in new folder
    #             new_head = head + '_' + \
    #                             '(' + str(storage.get(head)) + ')'  # create new file name head
    #             storage[new_head] = 1  # add new name to the storage
    #             print(curr_folder + '\\' + file_name)
    #             shutil.copy(curr_folder + '\\' + file_name,
    #                         new_folder_path + '\\' + new_head + '.' + tail)  # copy a file
    #             # with a new name into a new folder
    #             storage[head] += 1
    #         else:
    #             shutil.copy(curr_folder + '\\' + file_name,
    #                         new_folder_path + '\\' + file_name)
    #             storage[file_name] = 1
