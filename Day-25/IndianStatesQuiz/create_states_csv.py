import pandas as pd
# import turtle

PATH_TO_FILE = "100-python-projects/Day-25/IndianStatesQuiz/28_states.csv"
PATH_TO_IMG = "100-python-projects/Day-25/IndianStatesQuiz/india-outline-map.gif"

states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
]
# print(len(states))


# screen = turtle.Screen()
# screen.title("Indian States Game")
# image = PATH_TO_IMG
# screen.addshape(image)
# turtle.shape(image)

# def get_xy_coor(x,y):
#     print(f"{int(x)}, {int(y)}")
    
# screen.onscreenclick(get_xy_coor)

# screen.mainloop()

# Write the states list to a CSV file
df = pd.DataFrame(states)
df.to_csv(PATH_TO_FILE, index=False)



