import sys
import random

right_number = random.randint(int(sys.argv[1]), (int(sys.argv[2]) + 1))
while True:
    try:
        guess = int(input(f'Guess a number in range of {sys.argv[1]} to {sys.argv[2]} --> '))
        if guess < int(sys.argv[1]) or guess > int(sys.argv[2]):
            print('Out of range. Try once again.')
            continue
        else:
            if right_number == guess:
                print('Well done!')
                break
            else:
                print('Nope... Try once again.')
                continue
    except ValueError:
        print('Please enter a valid number.')
        continue
