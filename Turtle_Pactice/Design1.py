import colorsys
import turtle

turtle.bgcolor("black")
turtle.speed(0)

h=0
turtle.goto(100,200)
for i in range(25):
    turtle.color(colorsys.hsv_to_rgb(h,1,1))
    for i in range(75):
        h+=0.005
        turtle.forward(100)
        turtle.backward(100)
        turtle.right(1)
    turtle.forward(250)
turtle.done()

