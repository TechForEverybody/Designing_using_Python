import colorsys
import turtle

turtle.bgcolor("black")
turtle.speed(0)

h=0
turtle.goto(0,0)
for i in range(30):
    turtle.color(colorsys.hsv_to_rgb(h,1,1))
    for i in range(25):
        h+=0.005
        turtle.fd(100)
        turtle.bk(100)
        turtle.rt(10)
    turtle.fd(200)
turtle.done()

