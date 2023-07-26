#The name check.

# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.

first_name = "Anton"
input_name = "arton"
message = "name is right" if input_name == first_name or input_name == first_name.lower() else "your first name is incorrect, please change a name"
print(message)



#if input_name == first_name or input_name == first_name.lower():
#    message = "name is right"
#else:
#    message = "your first name is incorrect, please change a name"
