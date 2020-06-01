""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 5 """

import string

def count_attributes(string_in):
    char_counter, digit_counter, punct_counter = 0, 0, 0
    for char in string_in:
        if char in string.ascii_letters:
            char_counter += 1
        elif char in string.digits:
            digit_counter += 1
        elif char in string.punctuation:
            punct_counter += 1
    return char_counter, digit_counter, punct_counter


def main():
    string_input = "maria78!4*re''/54fe"
    print(f"The numbers of characters, digits and punctuation are (in this order): {count_attributes(string_input)}")


if __name__ == '__main__':
    main()
