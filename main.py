# main.py

# Specify the path to the file (replace with the actual path)
path_to_file = r"C:\Users\user\workspace\github.com\HamedGraphist\bookbot\books\frankenstein.txt"

# Use a with block to open the file
with open(path_to_file, 'r') as file:
    # Read the contents of the file into a string
    file_contents = file.read()

# Now you can work with the file_contents variable, which contains the content of the file
print(file_contents)
