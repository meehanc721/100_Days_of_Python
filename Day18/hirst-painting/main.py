import random
import turtle as t

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]

tim = t.Turtle()
t.colormode(255)


def line_of_dots():
    for i in range(10):
        tim.speed("fastest")
        tim.dot(20, random.choice(color_list))
        tim.forward(50)


def start_point(x, y):
    for i in range(10):
        tim.penup()
        tim.hideturtle()
        tim.goto(x, y)
        line_of_dots()
        y += 50             # make y start higher than previous by adding to negative integer
        tim.goto(x, y)


x_start = -430
y_start = -420
start_point(x_start, y_start)

screen = t.Screen()
screen.screensize(100, 100)
screen.exitonclick()
