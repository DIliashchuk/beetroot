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