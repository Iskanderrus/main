import sys
import random

right_number = random.randint(int(sys.argv[1]), (int(sys.argv[2]) + 1))
guess = int(input(f'Guess a number in range of {sys.argv[1]} to {sys.argv[2]} --> '))
while guess != right_number:
    if guess < int(sys.argv[1]) or guess > int(sys.argv[2]):
        guess = int(input('Out of range. Try once again: '))
    else:
        guess = int(input('Nope... Try once again: '))
else:
    print('Well done!')
