import random

word = input("Enter a word: ")

charlst = list(word)        # convert the string into a list of characters
random.shuffle(charlst)     # shuffle the list of characters randomly
new_word = ''.join(charlst) # convert the list of characters back into a string

print(new_word)