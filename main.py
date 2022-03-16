import turtle
from turtle import *
import random

tim = turtle.Turtle()
screen = Screen()
tim.hideturtle()
tim.speed(0)
turtle.colormode(255)

color_list = [(244, 231, 217), (208, 151, 103), (245, 226, 234), (218, 230, 239), (226, 241, 234), (58, 105, 133), (148, 87, 58), (128, 163, 185), (196, 137, 157), (138, 71, 95), (210, 91, 67), (130, 177, 155), (60, 120, 89), (162, 149, 54), (191, 91, 118), (224, 201, 126), (25, 48, 75), (78, 157, 122), (55, 41, 27), (232, 166, 185), (40, 56, 105), (238, 170, 159), (56, 33, 47), (58, 155, 172), (115, 37, 58), (105, 121, 164), (27, 51, 39), (160, 210, 190), (17, 95, 71), (117, 42, 33)]

tim.penup()
tim.setheading(220)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen.exitonclick()