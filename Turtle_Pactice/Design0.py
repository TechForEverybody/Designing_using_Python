import turtle
import colorsys

turtle.bgcolor("black")
turtle.setup(800,800)
turtle.speed(0)
turtle.tracer(10)
turtle.width(5)

for i in range(25):
    for j in range(25):
        turtle.color(colorsys.hsv_to_rgb(i/25,j/25,1))
        turtle.right(90)
        turtle.circle(200-i*4,90)
        turtle.left(90)
        turtle.circle(200-i*4,90)
        turtle.right(180)
        turtle.circle(50,15)
turtle.done()


