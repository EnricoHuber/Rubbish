""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 4 """
import string


def string_adjust(string_in):
    string_exit_lower = ""
    string_exit_upper = ""
    for char in string_in:
        if char in string.ascii_lowercase:
            string_exit_lower += char
        elif char in string.ascii_uppercase:
            string_exit_upper += char
    return string_exit_lower + string_exit_upper


def main():
    string_to_order = "CiaoAtuTTi"
    print(string_adjust(string_to_order))


if __name__ == '__main__':
    main()
