############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
import os


clear = lambda: os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(cards_list):
    card = cards_list[random.randint(0, len(cards_list) - 1)]
    return card


def calculate_score(list_of_cards):
    if sum(list_of_cards) >= 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
    return sum(list_of_cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Loose, opponent has BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21:
        return "You went over. You lose"
    elif dealer_score > 21:
        return "Opponent went over. You win"
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards =[]
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card(cards))
        dealer_cards.append(deal_card(cards))

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(dealer_cards)

        print(f'Your cards: {user_cards} and current score: {user_score}.')
        print(f'Computer\'s first card is: {dealer_cards[0]}.')

        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card(cards))
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        dealer_cards.append(deal_card(cards))
        computer_score = calculate_score(dealer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {dealer_cards}, computer's final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' of 'n': ") == 'y':
    clear()
    play_game()
