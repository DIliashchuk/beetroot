# The valid phone number program.

# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.

phone_number = "4212ууаа22212"

if phone_number.isdigit() and len(phone_number) == 10:
    message = "right"
elif phone_number.isdigit() and len(phone_number) != 10:
        message = "you need write 10 symbol in a phone number"
else:
    message = "please write correct number without symbols"
print(message)