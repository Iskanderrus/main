import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
game_over = False
number = random.randint(1, 100)

if level == "hard":
    attempts = 5
elif level == "easy":
    attempts = 10
else:
    game_over = True
    print("Wrong level. Game over.")

while not game_over:
    if game_over:
        break
    else:
        attempts_counter = attempts
        for x in range(attempts):
            print(f'You have {attempts_counter} attempts.')
            guess = input("Make a guess: ")
            if type(guess) != type(number):
                print("Wrong input of the number. You lose.")
                game_over = True
                break
            elif int(guess) < number:
                attempts_counter -= 1
                print("Too low.")
            elif int(guess) > number:
                attempts_counter -= 1
                print("Too high.")
            else:
                print(f"{number} is a right choice. You win.")
                game_over = True
                break
        else:
            game_over = True
            print("Out of attempts. You lose.")