""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 9 """ #Wrong
import string


def average(sum, n):
    return sum / n


def sum_and_average(str_in):
    sum_of_digits = 0
    counter = 0
    for char in str_in:
        if char in string.digits:
            sum_of_digits += int(char)
            counter += 1
    average_of_digits = sum_of_digits / counter
    return sum_of_digits, average_of_digits


def main():
    input_str = "Maria ha 24 anni ed è nata nel 1995"
    print(f"The sum and average of digits are: {sum_and_average(input_str)}")


if __name__ == '__main__':
    main()