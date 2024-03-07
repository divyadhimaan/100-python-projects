import random
import hangman_art
import hangman_words


chosen_word = random.choice(hangman_words.word_list)
word_len = len(chosen_word)
lives = 6

display = []
for x in range(word_len):
    display += "_"
print(f"Guess a {word_len} letter word")
print(f"You have {lives} lives.")

print(hangman_art.logo)

while lives:
    
    # asking user to guess a letter
    guess = input("Guess a letter: ").lower()
    is_guess_correct = False
    for index in range(word_len):
        if guess == chosen_word[index]:
            display[index] = guess;
            is_guess_correct = True
    if not is_guess_correct:
        print("------------------------")
        print("Wrong Guess. Lost a Live")
        lives -= 1
        print(f"Remaining Life/Lives: {lives}")
        print(hangman_art.stages[lives])
    print(display)
    if "_" not in display:
        print("You Won!")
        break
if lives == 0:
    print("Game Over. You lost!")
    print(f"Correct Word was {chosen_word}")