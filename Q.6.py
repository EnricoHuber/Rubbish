""" EXERCISES FROM https://pynative.com/python-exercises-with-solutions/ """

""" Question 6 """


def string_maker(s1, s2):
    string_out = ""
    s2 = s2[::-1]
    for i in range(min(len(s1), len(s2))):
        print(i)
        string_out = string_out + s1[i] + s2[i]
    if len(s1) > len(s2):
        string_out = string_out + s1[len(s2):]
    elif len(s2) > len(s1):
        s2 = s2[::-1]
        string_out = string_out + s2[0:len(s1)+1]
    return string_out


def main():
    print(string_maker("rino", "pala"))
#otsubra

if __name__ == '__main__':
    main()
