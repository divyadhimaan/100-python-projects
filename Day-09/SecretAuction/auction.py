from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidding_record = {}

def find_highest_bidder(bidding_record):
    max_bid = 0
    max_bidder = ""
    for key in bidding_record:
        if bidding_record[key] > max_bid:
            max_bid = bidding_record[key]
            max_bidder = key
    print(f"The winner is {max_bidder} with a bid of ${max_bid}.")

def start_bid():
    should_continue = True
    
    while should_continue:
        name = input("What is your name?: ")
        bid  = int(input("What's your bid?: $"))
        bidding_record[name] = bid
    
        is_continue = input("Are there any other bidders? Type \"yes\" or \"no\". ")
        if is_continue == "no":
            should_continue = False
        clear()

start_bid()
find_highest_bidder(bidding_record)