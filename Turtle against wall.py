import turtle
import random


def head_tail():
    head_tail_values = (0, 1)
    value_coin = random.choice(head_tail_values)
    return value_coin


def turtle_on_screen(turtle, screen)
    xTurtle, yTurtle = turtle.position()
    right = screen.window_width()/2 - 40
    left =


def turtle_moves(turtle_choice):
    if turtle_choice == 0:
        tess.right(90)
    else:
        tess.left(90)
    return tess


tess = turtle.Turtle()
tess.color("blue")
wn = turtle.Screen()
wn.bgcolor("green")
"""
print(campo.window_width())
print(campo.window_height())
print(turtle.position)
"""
while turtle_on_screen(tess, wn):


    value_coin = head_tail()
    tess = turtle_moves(value_coin)
    tess.forward(50)

wn.exitonclick()

if __name__ == '__main__':
    main()
