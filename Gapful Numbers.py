def is_gapful(num):
    divisor = str(num)[0] + str(num)[len(str(num)) - 1]
    if num % int(divisor) == 0:
        return True
    else:
        return False


def gapful_printer(upperbound):
    for n in range(100, upperbound + 1):
        if is_gapful(n):
            print(n)


def main():
    number = int(input("Insert the number: "))
    print(is_gapful(number))
    range_of_gapful = int(input("Insert the range in which you want all the gapful numbers: "))
    gapful_printer(range_of_gapful)


if __name__ == '__main__':
    main()
