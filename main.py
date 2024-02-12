import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
cars = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for i in range(15):
    cars[i] = CarManager()

for car in cars:
    for instance in cars:
        if car.distance(instance) < 15:
            new_y = randint(-260, 280)
            new_x = randint(-260, 320)
            car.goto(new_x, new_y)

screen.listen()
screen.onkey(tim.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move_forward(car.current_speed)
    for car in cars:
        if car.distance(tim) < 25:
            scoreboard.end_game()
            game_is_on = False
    if tim.ycor() > 280:
        tim.reset_position()
        for car in cars:
            car.current_speed = car.increase_speed(car.current_speed)
        scoreboard.next_lvl()








screen.exitonclick()
