""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 7 """


def string_balance_check(s1, s2):
    counter = 0
    if len(s1) >= len(s2):
        for char in s2:
            if char in s1:
                counter += 1
        if counter == len(s2):
            return True
        else:
            return False
    elif len(s2) > len(s1):
        for char in s1:
            if char in s2:
                counter += 1
        if counter == len(s1):
            return True
        else:
            return False

def main():
    string1 = "pinocchio"
    string2 = "chopin"
    print(string_balance_check(string1, string2))


if __name__ == '__main__':
    main()
