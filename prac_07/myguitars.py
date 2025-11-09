from guitar import Guitar


def main():
    guitars = []

    with open("guitars.csv", "r") as file:
        for line in file:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)


main()
