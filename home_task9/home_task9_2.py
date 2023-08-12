import sys

print(sys.path)

new_directory = "/Users/dmytroiliashchuk/PycharmProjects/beetroot_courses/home_task9/home_task9_2.py"
sys.path.append(new_directory)

print("Modified sys.path:", sys.path)
