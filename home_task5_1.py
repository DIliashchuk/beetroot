#The Guessing Game.

# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.



import random

print("Please try to guess the number")
player = input("Write number that I guess ")
computer = random.randint(1, 10)

if not player.isdigit():
    print("Please write number from 1 to 10")

if player == computer:
    print("You win")

else:
    print("You loose")
    print(computer)
