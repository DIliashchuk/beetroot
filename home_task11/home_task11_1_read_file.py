filename = "myfile.txt"

with open(filename, 'r') as file:
    contents = file.read()
    print(contents)