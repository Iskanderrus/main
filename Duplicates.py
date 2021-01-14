some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({dupl for dupl in some_list if some_list.count(dupl) > 1})

print(duplicates)