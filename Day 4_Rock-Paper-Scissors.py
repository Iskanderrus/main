import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

names = [rock, paper, scissors]

x = False
while not x:
    your_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    computer_choice = random.randint(0, 2)
    if int(your_choice) >= 3 or int(your_choice) < 0:
        print("Invalid input! You lose.")
        x = True
    elif int(your_choice) == 0 and computer_choice == 2:
        x = True
        print(f'You {names[int(your_choice)]}\nComputer {names[computer_choice]}\n You won.')
    elif int(your_choice) == 2 and computer_choice == 0:
        x = True
        print(f'You {names[int(your_choice)]}\nComputer {names[computer_choice]}\n You lost.')
    elif int(your_choice) == 2 and computer_choice == 1:
        x = True
        print(f'You {names[int(your_choice)]}\nComputer {names[computer_choice]}\n You won.')
    elif int(your_choice) == 1 and computer_choice == 2:
        x = True
        print(f'You {names[int(your_choice)]}\nComputer {names[computer_choice]}\n You lost.')
    elif int(your_choice) == 1 and computer_choice == 0:
        x = True
        print(f'You {names[int(your_choice)]}\nComputer {names[computer_choice]}\n You won.')
    elif int(your_choice) == 0 and computer_choice == 1:
        x = True
        print(f'You {names[int(your_choice)]}\nComputer {names[computer_choice]}\n You lost.')
    else:
        print("It's a draw! Try again.")
