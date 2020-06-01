"""
This code generates a 10x3 matrix filled with random numbers
within 0 and 1, and print the number nearest to 0.5 for each row
"""
import numpy as np
import random


def distance_from_half(num):
    return abs(num - 0.5)


def distance_check(dist, diff, num):
    if diff <= dist:
        return num, diff


def nearest_to_half_in_rows(row):
    """ Calculates the nearest to half for each row """
    for num in row:
        if row.index(num) == 0:
            distance = 0.5
            difference = distance_from_half(num)
            chosen_number, distance = distance_check(distance, difference, num)
        else:
            difference = distance_from_half(num)
            chosen_number, distance = distance_check(distance, difference, num)
    return chosen_number


def matrix_construction(n_rows, n_columns):
    row_selected = []
    matrix = np.zeros((n_rows, n_columns))
    for i in range(0, n_rows):
        for j in range(0, n_columns):
            matrix[i, j] = matrix[i, j] + random.random()
            row_selected.append(matrix[i, j])
        print(f"The nearest number to 0.5 in the row n.{i+1} is {nearest_to_half_in_rows(row_selected)}")
        row_selected = []
    print(matrix)


def main():
    matrix_rows = 10
    matrix_columns = 3
    matrix_construction(matrix_rows, matrix_columns)


if __name__ == '__main__':
    main()



