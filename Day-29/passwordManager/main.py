from tkinter import *
import pyperclip
from tkinter import messagebox
from random import choice, randint, shuffle
PATH_TO_IMG = "100-python-projects/Day-29/passwordManager/logo.png"
PATH_TO_FILE = "100-python-projects/Day-29/passwordManager/data.txt"
WHITE = "#fff"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(6, 8)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letter + password_numbers + password_symbols

    shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0, password)
    


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    
    if len(password)==0 or len(password)==0:
        messagebox.showerror(title="Insufficient Credentials", message="Please enter all the fields")
    else:  
    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \n Is ut okay to save?")
        if is_ok:
            with open(PATH_TO_FILE, mode="a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
            
            messagebox.showinfo(title="Saving", message="Credentials saved successfully.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file=PATH_TO_IMG)
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1,columnspan=2)
website_input.focus()

username_input = Entry(width=35)
username_input.grid(column=1, row=2,columnspan=2)
username_input.insert(0,"divya@gmail.com")

password_input = Entry(width=20)
password_input.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password",command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1, row=4,columnspan=2)

window.mainloop()