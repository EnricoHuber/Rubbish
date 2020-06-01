""" ESERCIZI DEL SITO https://www.programmareinpython.it/esercizi-python/ """

""" Esercizio n.23 """


def meters_to_miles(dist_meters):
    return (dist_meters/1609.344)


def meters_to_yard(dist_meters):
    return (dist_meters/0.9144)


def meters_to_feet(dist_meters):
    return (dist_meters/0.3048)


def meters_to_inches(dist_meters):
    return (dist_meters/0.0254)


def main():
    distance_in_meters = float(input("Insert the distance: "))
    print(f"{distance_in_meters} m corresponds to\n{meters_to_miles(distance_in_meters)} miles\n{meters_to_inches(distance_in_meters)} inches\n{meters_to_feet(distance_in_meters)} feet\n{meters_to_yard(distance_in_meters)} yards")


if __name__ == '__main__':
    main()
