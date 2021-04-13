import os

print("Welcome to secret auction program.")
progress = True

clear = lambda: os.system('clear')

bidders = {}

while progress:
    name = input("What is your name: ")
    bid = int(input("What is your bid? : "))
    bidders[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no' : ")
    clear()
    if others == "no":
        progress = False

max_bid = 0

for bidder in bidders:
    if bidders[bidder] > max_bid:
        max_bid = bidders[bidder]
        winner = bidder

print(f'Winner is {winner} with max bid was {max_bid}')
