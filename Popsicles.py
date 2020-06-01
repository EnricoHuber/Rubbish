def popsicles():
    n_siblings = int("Insert the number of siblings: ")
    n_popsicles = int("Insert the number of popsicles: ")
    if n_popsicles % n_siblings == 0:
        return "give away"
    else:
        return "eat them yourself"


def main():
    print(popsicles())


if __name__ == '__main__':
    main()