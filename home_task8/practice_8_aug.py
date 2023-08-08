import random

a , b = 5, 2

def pow (a, b):
    return a ** b

print(pow(a,b))


def random_list(len):
    list_rand = []
    for number in range(len):
        list_rand.append(random.randint(0, 100))
    return list_rand

print(random_list(20))

some_str = "mom clean rama"

def count_words(some_string):
    words = some_string.split()
    return len(words)

word_count = count_words(some_str)
print(word_count)


def is_sub(list_q):
    for item in list_q:
        if type(item) == list:
            return True
    return False

# Example usage
a = [1, 2, 3]
b = [1, 2, [3, 4, 5]]

print(is_sub(a))
print(is_sub(b))


def total_count(li: list) -> int:
    count = 0
    for item in li:
        if isinstance(item, list):
            count += total_count(item)
        else:
            count += 1
    return count

a = [1, 2, 3]
b = [1, 2, 3, [4, 5, 6]]
c = [1, 2, 3, [4, [1, 2], 6]]

print(total_count(c))

my_stack = {'data': [1, 2, 3, 4, 5]}

def stack_length(stack):
    return len(stack)

length = stack_length(my_stack)
print(f"Length of the stack: {length}")

def push(stack, element):
    stack['data'].append(element)
    return stack

# Приклад використання
my_stack = {'data': [1, 2, 3]}
new_element = 4
updated_stack = push(my_stack, new_element)
print("Оновлений стек:", updated_stack)

def pop(stack):
    if not stack['data']:
        raise IndexError("Stack is empty")
    element = stack['data'].pop()
    return element, stack

# Приклад використання
my_stack = {'data': [1, 2, 3, 4, 5]}
popped_element, updated_stack = pop(my_stack)
print(f"Видалений елемент: {popped_element}")
print("Оновлений стек:", updated_stack)


def print_stack(stack):
    if not stack['data']:
        print("Стек порожній")
        return

    elements = [str(item) for item in reversed(stack['data'])]
    formatted_stack = " -> ".join(elements)
    print("->", formatted_stack)


my_stack = {'data': [2, 4, 2, 1, 5, 55]}
print_stack(my_stack)





