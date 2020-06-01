""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 1 """


def string_out(string_in):

    half_index = len(string_in) // 2
    return string_in[(half_index - 1):(half_index + 2)]


def main():

    string_input = "percepire"
    print(string_out(string_input))


if __name__ == '__main__':
    main()
