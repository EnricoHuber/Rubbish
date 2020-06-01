import turtle


def dino_plotter():

    wn = turtle.Screen()
    wn.setworldcoordinates(-300, -300, 300, 300)
    alex = turtle.Turtle()
    f = open(r"mystery.txt", "r")

    for lines in f:
        item = lines.split()
        if item[0] == "UP":
            alex.up()
        elif item[0] == "DOWN":
            alex.down()
        else:
            alex.goto(int(item[0]), int(item[1]))
    wn.exitonclick()
    f.close()


def main():
    dino_plotter()


if __name__ == '__main__':
    main()
