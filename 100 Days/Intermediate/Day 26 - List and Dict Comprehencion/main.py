import random

"""
   ---List Comprehension---
Basic rule:
            new_list = [new_item for item in old_list]
"""

# List Comprehension Sample:
sides_of_squares = [1, 2, 3, 4, 5]
squares_areas = [item * item for item in sides_of_squares]
print(squares_areas)

# List Comprehension on String Sample:
name = "Alexander"
upper_letters_list = [letter.upper() for letter in name]
print(upper_letters_list)

# List Comprehension on a Range:
new_array = [item * 2 for item in range(0, 51)]
print(new_array)

"""
   ---Conditional List Comprehension:
Basic rule: 
            new_list = [new_item for item in old_list if condition]
"""

# Sample:
names = ["Alex", "Dave", "Beth", "Carolina", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
long_names = [name.upper() for name in names if len(name) > 4]
print(short_names)
print(long_names)

# Exercises
# 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squares_numbers = [number * number for number in numbers]
print(squares_numbers)

# 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [number for number in numbers if (number % 2 == 0)]
print(even_numbers)


# 3


def list_creator(file):
    with open(file, "r") as f:
        contents = f.readlines()
        new_list1 = []
        for item in contents:
            new_list1.append(item.strip())
        return new_list1


list1 = list_creator("file1.txt")
list2 = list_creator("file2.txt")

joint_list = list(set(int(item) for item in list2 if item in list1))
print(joint_list)

"""
   ---Dictionary Comprehension---
Basic rules:
            new_dict = {new_key:new_value for item in list}
            new_dict = {new_key:new_value for (key, value) in old_dict}
            new_dict = {new_key:new_value for (key, value) in old_dict if condition}
"""
scores_dict = {name: random.randint(0, 101) for name in names}
print(scores_dict)
