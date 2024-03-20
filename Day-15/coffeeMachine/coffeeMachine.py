from coffee_art import art
from coffee_recipe import Menu                 


resources = {
    "water": 1000,
    "milk": 800,
    "coffee": 800,
}
profit = 0

def enough_resources(required_ingredients):
    """Returns True when enough resources are available, otherwise False."""
    print("Checking for enough resources...")
    
    for resource in required_ingredients:
        if required_ingredients[resource] > resources[resource]:
            print(f"Oh-Uh, Not enough resources: {resource}. Call for maintenance")
            return False
    return True
    
def place_order(user_choice, order_ingredients):
    """Places order and reduces the resources available"""
    
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {user_choice} ☕️. Enjoy!")
   
def print_report():
    for item in resources:
        print(f"{item}: {resources[item]}")
    print(f"Money: {profit}")
    

def prompt(turned_on):
    global profit
    while turned_on:
        user_preference = input("Would you like to order or get the report or turn off the machine? (order/report/off):")
        if user_preference == "order":
            user_choice = input("What would you like to order? (espressso/latte/cappuccino):")
            resources_required = Menu[user_choice]["ingredients"]
            if enough_resources(resources_required):
                transaction_money = Menu[user_choice]["cost"]
                transaction_done = input(f"Please pay {transaction_money}$ by UPI. Type 'enter' when transaction completed: ")
                profit += transaction_money
                if transaction_done == "enter":
                    print(f"Placing your order for {user_choice} 🙂...")
                    place_order(user_choice,resources_required)
                
            
        elif user_preference == "report":
            print_report()
        elif user_preference == "off":
            turned_on = False
            print("Please visit again! 😃")
        else:
            print("Enter a valid user preference.")
    
def coffee_machine():  
    print("Welcome to the coffee machine.")
    print(art)
    prompt(turned_on = True)
    
coffee_machine()