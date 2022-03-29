import random
from turtle import Turtle, Screen

is_race_on = False
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
all_turtles = []


s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput("Make your bet!", "Which color of turtle will win the race? ")
print(user_bet)
start_pos = 150

for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    start_pos = start_pos - 40
    t.goto(x=-230, y=start_pos)
    all_turtles.append(t)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've win! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


s.exitonclick()