#Words combination

#Create a program that reads an input string
#and then creates and prints 5 random strings from characters of the input string.

#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters

import random

word = input("Enter a word: ")

i = 0
while i < 5:
    charlst = list(word)        # convert the string into a list of characters
    random.shuffle(charlst)     # shuffle the list of characters randomly
    new_word = ''.join(charlst) # convert the list of characters back into a string
    print(new_word)
    i +=1

# I'm proud of you) nice usage of join. good understanding of convetring of string to the list
