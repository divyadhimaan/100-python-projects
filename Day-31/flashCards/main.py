from tkinter import *
import pandas as pd
import random

PATH_TO_IMG_FOLDER="100-python-projects/Day-31/flashCards/images"
PATH_TO_ORIGINAL_FILE="100-python-projects/Day-31/flashCards/data/french_words.csv"
PATH_TO_LEARN_FILE="100-python-projects/Day-31/flashCards/data/words_to_learn.csv"
FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- HANDLE DATA ------------------------------- #
try:
    data = pd.read_csv(PATH_TO_LEARN_FILE)
except FileNotFoundError:
    data = pd.read_csv(PATH_TO_ORIGINAL_FILE)

to_learn_list = data.to_dict(orient="records")
current_card = {}
    

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_list)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
    
def is_known():
    to_learn_list.remove(current_card)
    print(len(to_learn_list))
    data = pd.DataFrame(to_learn_list)
    data.to_csv(PATH_TO_LEARN_FILE, index=False)
    next_card()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

# canvas widget
canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file=f"{PATH_TO_IMG_FOLDER}/card_front.png")
card_back_img = PhotoImage(file=f"{PATH_TO_IMG_FOLDER}/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)


# Labels
card_title = canvas.create_text(400,150, text="", fill="black", font=(FONT_NAME, 40, "italic"))
card_word = canvas.create_text(400,263, text="", fill="black", font=(FONT_NAME, 60, "bold"))

# Button
wrong_button_img = PhotoImage(file=f"{PATH_TO_IMG_FOLDER}/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0,command=next_card)
wrong_button.grid(column=0, row=1)

known_button_img = PhotoImage(file=f"{PATH_TO_IMG_FOLDER}/right.png")
known_button = Button(image=known_button_img, highlightthickness=0,command=is_known)
known_button.grid(column=1, row=1)

next_card()
window.mainloop()