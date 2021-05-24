# # extracting color
# import colorgram
#
# numbers_of_colors = 110
# colors = colorgram.extract('image.jpg', numbers_of_colors)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle as t
import random

t.colormode(255)
color_list = [(228, 225, 222), (229, 147, 85), (217, 227, 219), (119, 166, 186), (160, 13, 19), (232, 221, 226), (30, 110, 159), (235, 81, 44), (215, 222, 228), (5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144), (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77), (13, 64, 41), (137, 83, 98), (83, 17, 24), (46, 168, 74), (3, 66, 140), (173, 133, 149), (36, 25, 21), (45, 151, 198), (220, 63, 68), (227, 171, 162), (73, 135, 188), (172, 204, 174)]
timmy = t.Turtle()
timmy.speed("fastest")
timmy.hideturtle()

timmy.penup()
timmy.setposition(-250, -250)
timmy.pendown()

for move in range(0, 500, 50):
    for step in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    timmy.setposition(-250, -200 + move)

my_screen = t.Screen()
my_screen.exitonclick()