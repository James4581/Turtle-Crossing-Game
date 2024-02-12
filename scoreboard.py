from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-200, 270)
        self.color("black")
        self.hideturtle()
        self.update_scoreboard()

    def end_game(self):
        self.clear()
        self.goto(-100, 0)
        self.write(f"Game Over. Final score: {self.score}", font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", font=FONT)

    def next_lvl(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

