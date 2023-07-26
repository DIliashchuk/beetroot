phone_number = "4212ууаа22212"

if phone_number.isdigit() and len(phone_number) == 10:
    message = "right"
elif phone_number.isdigit() and len(phone_number) != 10:
        message = "you need write 10 symbol in a phone number"
else:
    message = "please write correct number without symbols"
print(message)