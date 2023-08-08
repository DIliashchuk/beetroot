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