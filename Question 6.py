import math

c, h = 50, 30

my_list = input('Enter numbers separated by a comma ')
numbers = my_list.split(',')
squares = []

for d in numbers:
    squares.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(squares))