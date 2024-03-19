from art import logo, vs
from game_data import data
import random
from replit import clear

def pick_data():
    return random.choice(data)
    
def format_data(item):
    name = item["name"]
    description = item["description"]    
    country = item["country"]
    return f"{name}, a {description}, from {country}."
    
def check_guess(item_1, item_2, guess):
    followers_1 = item_1["follower_count"]
    followers_2 = item_2["follower_count"]

    correct_ans = followers_1 if followers_1 > followers_2 else followers_2

    return (
        (guess == "A" and item_1["follower_count"] == correct_ans) or (guess == "B" and item_2["follower_count"] == correct_ans)
    )
        

    

def play(item_1, score):
    
    item_2 = pick_data()
    while item_2 == item_1:
        item_2 = pick_data()

    # print data
    print(f"Compare A: {format_data(item_1)}")
    print(vs)
    print(f"Against B: {format_data(item_2)}")

    # ask for guess and check it
    guess = input("Who has more followers? Type 'A' or 'B':")
    is_correct_ans = check_guess(item_1, item_2, guess)
    
    if is_correct_ans:
        clear()
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}.")
        play(item_2, score)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")

print(logo)
item_1 = pick_data()
play(item_1, 0)

    
    
