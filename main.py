import turtle as t
import random

# import colorgram

toby = t.Turtle()
t.colormode(255)
toby.speed("fastest")
toby.pensize(15)
color_list =[(200, 10, 35), (247, 236, 37), (239, 231, 3), (36, 216, 77), (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161)]

for y in range(-200, 251, 50):
    for x in range(-200, 251, 50):
        toby.setpos(x,y)
        toby.dot(random.choice(color_list))
        toby.pendown()
        toby.penup()



screen = t.Screen()
screen.exitonclick()
    
    
    
  

    


