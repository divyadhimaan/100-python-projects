from turtle import Turtle
import time

LIVES = 5
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")
PATH = "100-python-projects/Day-24/snakeGame/score.txt"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        with open(PATH) as score_file:
            content = score_file.read()
        self.high_score = int(content)
        self.lives = LIVES
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score} | Lives: {self.lives}", align=ALIGNMENT, font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.lives -= 1
        self.update_scoreboard()  
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)
        with open(PATH, mode="w") as score_file:
            score_file.write(f"{self.high_score}")
           
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    
        