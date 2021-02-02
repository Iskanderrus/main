x, y = map(int, input('Enter here two digits separated by comma: ').split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i * j)
    lst.append(tmp)

print(lst)
