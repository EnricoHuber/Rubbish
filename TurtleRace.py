import random
import turtle

campo = turtle.Screen()
campo.bgcolor("lightgreen")

tess = turtle.Turtle()
alex = turtle.Turtle()
tess.color("blue")
alex.color("red")
tess.shape("turtle")
alex.shape("turtle")
tess.up()
alex.up()
tess.right(180)
tess.forward(100)
tess.right(180)
alex.right(180)
alex.forward(100)
alex.right(180)
tess.left(90)
tess.forward(30)
tess.right(90)
for i in range(20):
    tess.forward(random.randrange(1, 20))
    alex.forward(random.randrange(1, 20))

campo.exitonclick()
