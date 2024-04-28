"""file providing code to extract and print file information from the current working directory""" 

import os

# Initialize an empty list to store file information
file_list = []

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# path = directory path, dir = directory, files = file
for path, dir_name, files in os.walk(thisdir):
    # Create a dictionary containing path, name, and size
    for file in files:
        file_dict = {
            'path': os.path.join(path, file),
            'name': file,
            'size': os.path.getsize(os.path.join(path, file))
        }
        # Add the dictionary to the file_list
        file_list.append(file_dict)
# Print the list of dictionaries, with each dictionary on a new line
print(*file_list, sep='\n')
