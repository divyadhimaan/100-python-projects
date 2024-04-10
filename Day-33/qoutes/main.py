from tkinter import *
import requests
PATH_TO_BG_IMG = "100-python-projects/Day-33/qoutes/background.png"
PATH_TO_IMG = "100-python-projects/Day-33/qoutes/kanye.png"
API_ENDPOINT = "https://api.kanye.rest/"

def get_quote():
    response = requests.get(url=API_ENDPOINT)
    response.raise_for_status()
    
    data = response.json()
    quote = data["quote"]
    if len(quote) < 100:
        canvas.itemconfig(quote_text, text=quote)
    else:
        get_quote()



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50,bg="white")

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=PATH_TO_BG_IMG)
canvas.create_image(150, 207, image=background_img)
canvas.config(highlightthickness=0, bg= "white")
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=PATH_TO_IMG)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()