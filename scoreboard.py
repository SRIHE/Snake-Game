from turtle import Turtle
from food import Food
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score: {self.score}",align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!", align="center", font=("Arial", 24, "normal"))
        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
    
    