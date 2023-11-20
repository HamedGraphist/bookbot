path_to_file = "C:\\Users\\user\\workspace\\github.com\\HamedGraphist\\bookbot\\books"

# Use a with block to open the file
with open(path_to_file, 'r') as file:
    # Read the contents of the file into a string
    file_contents = file.read()

# Now you can work with the file_contents variable, which contains the content of the file
print(file_contents)