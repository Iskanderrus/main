import random
names_string = input("Give me everybody's People, separated by a comma: ")
names = names_string.split(", ")

print(f"{names[random.randint(0, (len(names) - 1))]} is paying for all.")
