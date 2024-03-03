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

import random

choices = [rock, paper, scissors]

print("Welcome to the Rock, Paper, Scissors Game!")
print("You will get 5 matches.")
valid_option = [0,1,2]
match = 0
wins = 0
draws = 0
while(match != 5):
    
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice not in valid_option:
        print("pick a valid option.")
        continue
    print(f"You chose {user_choice}")
    print(choices[user_choice])
    
    comp_choice = random.randint(0,2)
    print(f"Computer chooses {comp_choice}")
    print(choices[comp_choice])
    if user_choice == comp_choice:
        print("That's a Draw.")
        draws += 1
    if (user_choice == 0 and comp_choice == 2) or (user_choice > comp_choice):
        print(f"You Won Match: {match} :)")
        wins += 1
    else:
        print(f"You lost Match: {match}. :(")

    match += 1


print("That is the end of 5 Matches.")
print("Leaderboard:")
print(f"Matches Won: {wins}\n Matches Lost: {5-wins-draws}\n Matches Drawn: {draws}")