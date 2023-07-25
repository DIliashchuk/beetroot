import random

print("Please try to guess the number")
player = input("Write number that I guess ")
computer = random.randint(1, 10)

if player == computer:
    print("You win")
else:
    print("You loose")
    print(computer)
