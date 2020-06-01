""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 2 """


def string_insert(s_1, s_2):
    half_index = len(s_1) // 2
    return s_1[:(half_index - 1)] + s_2 + s_1[half_index:]


def main():
    string_one = "pastasciutta"
    string_two = "caldezzasc"
    print(string_insert(string_one, string_two))


if __name__ == '__main__':
    main()
