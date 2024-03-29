from turtle import Turtle
import time
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)
            
        
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        
    def reset(self):
        self.clear()
        self.__init__(self.best_score)
        