from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        game_over = Turtle("turtle")
        game_over.color("black")
        game_over.penup()
        game_over.hideturtle()
        game_over.clear()
        game_over.goto(-100, 0)
        game_over.write(f"GAME OVER", align="left", font=FONT)
