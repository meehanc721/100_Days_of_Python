from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.current_score = 0
        self.update_score()

    def increase_score(self):
        self.clear()
        self.current_score += 1
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

