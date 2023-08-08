#List comprehension exercise

#Use a list comprehension to make a list containing tuples (i, j)
# where 'i' goes from 1 to 10 and 'j' is corresponding to 'i' squared.

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_square = [x**2 for x in list_numbers]

for y, element in enumerate(list_square):
    print(y+1, element)
