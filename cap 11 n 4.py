import turtle
import numpy as np


def angular_coefficient(list_x, list_y):
    sum_xi_yi = 0
    sum_xi_squared = 0

    nx_mean_y_mean = len(list_x)*np.mean(list_x)*np.mean(list_y)
    nx_mean_squared = len(list_x)*np.mean(list_x)**2
    for i in range(len(list_x)):
        sum_xi_yi += list_x[i]*list_y[i]
        sum_xi_squared += list_x[i]**2
    return (sum_xi_yi - nx_mean_y_mean)/(sum_xi_squared - nx_mean_squared)


def regline_plotter(turt, screen, list_x_pos, list_y_pos):
    angular_coeff = angular_coefficient(list_x_pos, list_y_pos)
    list_x_pos.sort()
    n_points = len(list_x_pos)
    for i in range(n_points):
        turt.goto(list_x_pos[i], np.mean(list_y_pos + angular_coeff*(list_x_pos[i] - np.mean(list_x_pos))))
        turt.down()
    return screen


def plot_regression():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.shape("circle")
    f = open(r"C:\Users\Enrico\PycharmProjects\ClassProjects\Programming Laboratory\Esercizi\CLASS\labdata.txt", "r")
    x_pos = []
    y_pos = []
    for line in f:
        items = line.split()
        x_pos.append(int(items[0]))
        y_pos.append(int(items[1]))
    wn.setworldcoordinates(min(x_pos) - 10, min(y_pos) - 10, max(x_pos) + 10, max(y_pos) + 10)
    flag = False
    t.up()
    for x, y in zip(x_pos, y_pos):
        if flag:
            t.setposition(x, y)
            t.stamp()
        else:
            t.stamp()
            flag = True
    wn = regline_plotter(t, wn, x_pos, y_pos)
    wn.exitonclick()


def main():
    f = open(r"C:\Users\Enrico\PycharmProjects\ClassProjects\Programming Laboratory\Esercizi\CLASS\labdata.txt", "r")
    plot_regression()


if __name__ == '__main__':
    main()
