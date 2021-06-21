# my_list = [2, 3, 4]
#
# print(list(map(lambda item: item * item, my_list)))
#
# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# print(list(filter(lambda item: sorted(a).item[1], a)))


# def evaporator(content, evap_per_day, threshold):
#     idx = 0
#     minv = content * (threshold / 100)
#     while content > minv:
#         content = content - content * (evap_per_day / 100)
#         idx += 1
#     return idx
#
#
# evaporator(100, 10, 5)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for _ in range(nr_letters)]
print(password_letters)
password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
print(password_numbers)
password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
print(password_symbols)
password_list = password_letters + password_numbers + password_symbols
print(password_list)
random.shuffle(password_list)
print(password_list)

password = "".join(password_list)

print(password)
