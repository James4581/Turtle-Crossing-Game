from turtle import Turtle, Screen
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.penup()
        self.current_speed = STARTING_MOVE_DISTANCE
        self.goto(300, randint(-260, 280))
        self.setheading(180)
        self.move_forward(self.current_speed)

    def increase_speed(self, current_speed):
        current_speed += MOVE_INCREMENT
        return current_speed
    def reset_position(self):
        self.hideturtle()
        self.goto(290, randint(-260, 280))
        self.showturtle()

    def move_forward(self, current_speed):
        if self.xcor() < -280:
            self.reset_position()
        new_x = self.xcor() - current_speed
        self.goto(new_x, self.ycor())




