import random

x = False
while not x:
    random_integer = random.randint(0, 1)
    prompt = input("Guess 'Heads' or 'Tails'\n")

    if random_integer == 0:
        result = 'Heads'
    else:
        result = 'Tails'

    if prompt == result:
        print(f" You won. It really was {result}")
        x = True
    else:
        print(f"Oh no.. it was {result} and you told {prompt}")
