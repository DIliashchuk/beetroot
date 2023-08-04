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

# Fine


# Exclusive common numbers.

# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers

list_one = []
list_two = []
i = 0
while i < 10:
    number_list1 = random.randint(1, 10)
    list_one.append(number_list1)
    number_list2 = random.randint(1, 10)
    list_two.append(number_list2)
    i += 1
print(list_one, list_two)
final_list = set(list_one + list_two)
print(final_list)

# fine that you remember about sets)

#Extracting numbers.

#Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.

#Constraint: use only while loop for iteration

# Create a list containing all integers from 1 to 100
all_integers = []
i = 1
while i < 101: # can be replaces with "list(range(101))"
    all_integers.append(i)
    i += 1
print(all_integers)
# Find integers that are divisible by 7 but not a multiple of 5
filtered_integers = [num for num in all_integers if num % 7 == 0 and num % 5 != 0] # nice usage of list comprehension

# Print the list of filtered integers
print(filtered_integers)


#fine but see the comments