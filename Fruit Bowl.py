def apple_needed(total_of_fruit):
    return round((total_of_fruit/2)/3)


def main():
    n_fruits = int(input("Insert the number of fruits: "))
    print(f"You can make {apple_needed(n_fruits)} pie out of {n_fruits//2} apples")


if __name__ == '__main__':
    main()
