# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     rgb_colors.append(color.rgb)

# print(rgb_colors)

# from turtle import Turtle, Screen
import turtle as t
import heroes

print(heroes.gen())
toby = t.Turtle()
toby.shape("turtle")
toby.color("green", "yellow")

for _ in range(4):
    toby.forward(100)

    toby.right(90)


screen = t.Screen()
screen.exitonclick()
