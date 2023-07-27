# Make a program that has some sentence (a string) on input and returns a dict containing
# all unique words as keys and the number of occurrences as values.

input_sentence = input("Please, write a sentence ")
split_words = input_sentence.split()
dictionary_words = dict()


for line in split_words:
    words = line.split(" ")
    for word in words:
        if word in dictionary_words:
            dictionary_words[word] = dictionary_words[word] + 1
        else:
            dictionary_words[word] = 1


for key in list(dictionary_words.keys()):
    print(key, ":", dictionary_words[key])



#dict_words = dict(enumerate(split_words))
#print(dict_words)


# Compute the total price of the stock
# where the total price is the sum of the price of an item multiplied by the quantity of this exact item.

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total = 0
for x in prices:
    total = total + prices[x] * stock[x]
print(total)

#List comprehension exercise

#Use a list comprehension to make a list containing tuples (i, j)
# where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_square = [x**2 for x in list_numbers]

for y, element in enumerate(list_square):
    print(y+1, element)


#task4

list_weekend = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day, number in enumerate(list_weekend):
    print(day+1, number)

