"""
This code generates a 10x3 matrix filled with random numbers
within 0 and 1, and print the number nearest to 0.5 for each row
"""
import numpy as np
import random


def distance_from_half(num):
    return abs(num - 0.5)


def nearest_to_half_in_rows(row):
    """ Calculates the nearest to half for each row """
    for num in row:
        if row.index(num) == 0:
            distance = 0.5
            difference = distance_from_half(num)
            if difference <= distance:
                chosen_number = num
                distance = difference
        else:
            difference = distance_from_half(num)
            if difference <= distance:
                chosen_number = num
                distance = difference
    return chosen_number


def matrix_construction(n_rows, n_columns):
    row_selected = []
    matrix = np.zeros((n_rows, n_columns))
    for i in range(0, n_rows):                      # Iterates through rows
        for j in range(0, n_columns):               # Iterates through columns
            matrix[i, j] = matrix[i, j] + random.random()
            row_selected.append(matrix[i, j])       # Creates a list of numbers for each row
        print(f"The nearest number to 0.5 in the row n.{i+1} is {nearest_to_half_in_rows(row_selected)}")
        row_selected = []
    print(matrix)


def main():
    matrix_rows = 10
    matrix_columns = 3
    matrix_construction(matrix_rows, matrix_columns)


if __name__ == '__main__':
    main()
