from replit import clear
from art import logo
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list_of_cards):
    """ Take a list of cards and return the score calculated from the cards.
    Also checks for blackjack and ace.
    """
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0;

    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)
        
    return sum(list_of_cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    

def play(): 
    print(logo)
    computer_cards = []
    user_cards = []
    computer_total = -1
    user_total = -1
    is_game_over = False

    
    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while not is_game_over:
        computer_total = calculate_score(computer_cards)
        user_total = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_total}")
        print(f"Computer's first card: {computer_cards[0]}")
    
        
    
        if computer_total == 0 or user_total == 0 or user_total > 21:
            is_game_over = True
        else:
            user_wants_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_wants_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_total != 0 and computer_total < 17:
        computer_cards.append(deal_card())
        computer_total = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_total}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_total}")
    print(compare(user_score=user_total, computer_score=computer_total))

while input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play()