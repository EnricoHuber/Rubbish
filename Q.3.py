""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 3 """


def half_index(string_in):
    return len(string_in) // 2


def string_out(s1, s2):
    str_out = s1[0] + s2[0] + s1[half_index(s1)-1] + s2[half_index(s2) - 1] + s1[len(s1) - 1] + s2[len(s2) - 1]
    return str_out


def main():
    print(string_out("emote", "fazzone"))


if __name__ == '__main__':
    main()
