""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.22 """


def min_to_sec(min):
    return min * 60


def hour_to_sec(hour):
    return hour * 3600


def day_to_sec(day):
    return day * 3600 * 24


def second_converter(x):
    if x == 'm':
        minutes = float(input("How many minutes?: "))
        return f"{minutes} minutes corresponds {min_to_sec(minutes)} seconds"
    elif x == 'h':
        hours = float(input("How many hours?: "))
        return f"{hours} hours corresponds to {hour_to_sec(hours)} seconds"

    elif x == 'd':
        days = float(input("How many days?: "))
        return f"{days} days corresponds to {day_to_sec(days)} seconds"
    else:
        return "Not a valid input!"


def main():
    choice = input("Insert if you want to convert from\nMinutes (type 'm')\nHours (type 'h')\nDays (type 'd')\n")
    print(second_converter(choice))


if __name__ == '__main__':
    main()
