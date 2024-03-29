from tkinter import *


def button_clicked():
    input_text = input.get()
    my_label.config(text =input_text)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="A label", font=("Arial", 24, "bold"))
my_label.pack() # every widget needs to be packed or it won't show up
# my_label.pack(expand=True)

# for changing the values
# my_label["text"] = "new text"
my_label.config(text = "new txt")

# Button

button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()


# keeps window in a loop to listen for user interactions
window.mainloop()