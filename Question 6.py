import math

c, h = 50, 30

my_list = input('Enter numbers separated by a comma ').split(',')
squares = []

for d in my_list:
    squares.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
print(','.join(squares))