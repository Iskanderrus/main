my_list = [2, 3, 4]

print(list(map(lambda item: item * item, my_list)))

a = [(0,2), (4,3), (9,9), (10,-1)]
print(list(filter(lambda item: sorted(a).item[1], a)))