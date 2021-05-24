from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()

# # draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# # Draw a dashed line
# for _ in range(10):
#     timmy.forward(5)
#     timmy.color("white")    # or timmy.penup()
#     timmy.forward(5)
#     timmy.color("black")    # or timmy.pendown()

# # 畫三角形～八邊形
# for number in range(3, 11):
#     for times in range(0, number):
#         timmy.forward(100)
#         timmy.right(360 / number)

# # Draw a random walk
# colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# angle = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed("fastest")
#
# for _ in range(200):
#     timmy.forward(30)
#     timmy.color(random_color())
#     timmy.right(random.choice(angle))

# # Make a Spirograph
# timmy.speed("fastest")
# def draw_a_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         timmy.color(random_color())
#         timmy.setheading(timmy.heading() + size_of_gap)
#         timmy.circle(40)
# draw_a_spirograph(10)


# my_screen = Screen()
# my_screen.exitonclick()