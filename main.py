# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)

from turtle import Turtle, Screen
import random

toby = Turtle()


toby.hideturtle()

colors = [
    "hot pink",
    "dark orange",
    "yellow",
    "lime",
    "light sky blue",
    "indigo",
    "dark magenta",
    "turquoise",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        toby.forward(100)
        toby.right(angle)


for shape_side_n in range(3, 11):
    toby.color(random.choice(colors))
    draw_shape(shape_side_n)


    
    
    
  

    



screen = Screen()
screen.exitonclick()
