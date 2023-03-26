import os

# Specify the path to the file
file_path = 'price.txt'

# Check if the file exists
if os.path.exists(file_path):
    # Delete the file
    os.remove(file_path)
    print(f'{file_path} deleted successfully.')
else:
    print(f'{file_path} does not exist.')