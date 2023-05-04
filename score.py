
from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.pencolor("white")
        self.goto(0,270)
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 23, 'normal'))

    def detect_food(self):
        self.clear()
        self.score +=1
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, align="center", font=('Arial', 23, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", True, align="center", font=('Arial', 25, 'normal'))
