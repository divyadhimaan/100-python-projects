import turtle
import pandas as pd

PATH_TO_FILE = "100-python-projects/Day-25/IndianStatesQuiz/28_states.csv"
PATH_TO_IMG = "100-python-projects/Day-25/IndianStatesQuiz/india-outline-map.gif"
PATH_TO_NEW_FILE = "100-python-projects/Day-25/IndianStatesQuiz/states_to_learn.csv"

screen = turtle.Screen()
screen.title("Indian States Game")
image = PATH_TO_IMG
screen.addshape(image)
turtle.shape(image)

# def get_xy_coor(x,y):
#     print(f"{int(x)}, {int(y)}")
    
# screen.onscreenclick(get_xy_coor)

# screen.mainloop()

# clearing the resulting file
empty_df = pd.DataFrame()
empty_df.to_csv(PATH_TO_NEW_FILE, index=False)

data = pd.read_csv(PATH_TO_FILE)
all_states = data.state.to_list()

guessed_states = []
while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv(PATH_TO_NEW_FILE)
        break
    if answer_state in all_states: 
        guessed_states.append(answer_state)
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup() 
        state_data = data[data.state == answer_state]
        tim.goto(int(state_data.x), int(state_data.y))
        tim.write(state_data.state.item())






