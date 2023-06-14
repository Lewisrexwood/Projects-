from turtle import Turtle

SCORE = 0


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.clear()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def Game_Over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))

    def again(self):
        self.goto(0, -20)
        self.write(f"Click to start start again", align="center", font=("Arial", 20, "normal"))



