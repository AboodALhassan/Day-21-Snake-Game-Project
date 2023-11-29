from turtle import Turtle
ALIGMENT = "center"
FONT = ('Courier', 18, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(-10, 270)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGMENT, font=FONT)
        self.score += 1

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align=ALIGMENT, font=FONT)
