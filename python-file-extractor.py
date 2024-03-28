import os

# Initialize an empty list to store file information
file_list = []

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r = root, d = directories, f = files
for path, dir, files in os.walk(thisdir):
        # Create a dictionary containing file path and name
        for file in files:
                file_dict = {
                    'path': os.path.join(path, file),
                    'name': file,
                    'size': os.path.getsize(os.path.join(path, file))
                }
                # Add the dictionary to the file_list
                file_list.append(file_dict)
# Print the list of dictionaries, each containing file information
print(*file_list, sep='\n')
