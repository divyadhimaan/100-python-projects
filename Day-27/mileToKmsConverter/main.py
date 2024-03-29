from tkinter import *


def miles_to_kms():
    miles = float(miles_input.get())
    kms = miles * 1.60934
    result_label.config(text =f"{kms}")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

km_result_label = Label(text="Km")
km_result_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_kms)
button.grid(column=1, row=2)




# keeps window in a loop to listen for user interactions
window.mainloop()