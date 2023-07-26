#The greatest number

#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers

import random

#number = random.randint(1, 100)
list = []
i = 0
while i < 10:
    number = random.randint(1, 100)
    list.append(number)
    i += 1
print(list)
print(max(list))