# String manipulation
#
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.

input_text = "my"
if len(input_text) >= 2:
    print(input_text[0] + input_text[1] + input_text[-2] + input_text[-1])
else:
    print("Empty String")

# fine, but input build-in funcion can be used for defining input text