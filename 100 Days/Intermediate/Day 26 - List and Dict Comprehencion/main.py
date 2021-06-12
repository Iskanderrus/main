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

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squares_numbers = [number * number for number in numbers]
print(squares_numbers)


