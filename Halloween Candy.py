def dollar_percentage(total):
    return round((2/total)*100, 2)


def main():
    n_houses = int(input("Insert the number of houses visited: "))
    print(f"The chance to take a dollar bill is {dollar_percentage(n_houses)} %")


if __name__ == '__main__':
    main()
