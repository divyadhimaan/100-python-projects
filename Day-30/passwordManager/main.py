from tkinter import *
import pyperclip
from tkinter import messagebox
import time
import json,os
from random import choice, randint, shuffle
PATH_TO_IMG = "100-python-projects/Day-30/passwordManager/logo.png"
PATH_TO_FILE = "100-python-projects/Day-30/passwordManager/data.json"
WHITE = "#fff"
# ----------------------------SEARCH PASSWORD ------------------------------- #
def search():
    website = website_input.get()
    try:
        with open(PATH_TO_FILE, "r") as data_file:
            data = json.load(data_file)
    except KeyError:
        messagebox.showerror(title="Alert", message="No data found")
    except FileNotFoundError:
        messagebox.showerror(title="Alert", message="No passwords stored yet.")
    else:
        if website in data.keys():
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Alert", message="No record for this website exists.") 
        



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
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(password)==0 or len(website)==0:
        messagebox.showerror(title="Insufficient Credentials", message="Please enter all the fields")
    else:
        try:
            with open(PATH_TO_FILE, mode="r") as data_file:
                # reading json file
                data = json.load(data_file)
        except FileNotFoundError:
            with open(PATH_TO_FILE, mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
                
        else:       
            # updating data
            data.update(new_data)

            with open(PATH_TO_FILE, mode="w") as data_file:
                # writing data
                json.dump(data, data_file, indent=4)
                print("File successfully written.")
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()
       

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
website_input = Entry(width=20)
website_input.grid(column=1, row=1)
website_input.focus()

email_input = Entry(width=42)
email_input.grid(column=1, row=2,columnspan=2)
email_input.insert(0,"divya@gmail.com")

password_input = Entry(width=20)
password_input.grid(column=1, row=3)

# Button
search_button = Button(text="Search",width=18,command=search)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password",width=18,command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",width=42, command=save)
add_button.grid(column=1, row=4,columnspan=2)

window.mainloop()