# The birthday greeting program.

# Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”

while True:
    name = input("What is your name? ")
    if name.isdigit():
        print("Please write the name, not number")
    else:
        break
while True:
    age = input("How old are you? ")
    if not age.isdigit():
        print("Please write number, not name")
    else:
        break
print("Hello", name.capitalize(), "on your next birthday you’ll be", int(age) + 1, "years ")

# very good