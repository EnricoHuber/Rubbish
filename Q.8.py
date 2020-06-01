""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 8 """


def occurrence_counter(str_in, substr_in):
    return str_in.lower().count(substr_in.lower())


def main():
    input_str = "Welcome to USA. usa is awesome, more than Usa itself. You should visit Usa!"
    input_substr = "usa"
    print(occurrence_counter(input_str, input_substr))


if __name__ == '__main__':
    main()
