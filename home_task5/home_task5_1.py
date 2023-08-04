#The Guessing Game.

# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.



import random

print("Please try to guess the number")
print("Can you guess the number? Let's try")
player = input("Choose a number from 1 to 10 ")
if player.isdigit():
    computer = random.randint(1, 10)
    print(("Computer number:"), computer)
    player_1 = int(player)
    if computer == player_1:
        print("You Win!")
    else:
        print("You lose!")
else:
    print("You need the number, start New Game!")

#ok, fine that you make isdigit check