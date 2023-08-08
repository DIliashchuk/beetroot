#task4

list_weekend = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Створити словник {1: "Monday", 2: "Tuesday", ...}
dict_weekday_to_number = {day+1: day_name for day, day_name in enumerate(list_weekend)}
print(dict_weekday_to_number)

# Створити зворотний словник {"Monday": 1, "Tuesday": 2, ...}
dict_number_to_weekday = {day_name: day+1 for day, day_name in enumerate(list_weekend)}
print(dict_number_to_weekday)