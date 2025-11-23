from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("limo", 100, 2),
             SilverServiceTaxi("Truck", 200, 4)]

    bill_to_date = 0
    current_taxi = None

    menu()
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")

            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxi[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")

            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            trip_cost = current_taxi.get_fare()
            bill_to_date += trip_cost

        else:
            print("Invalid option")

        print(f"bill to date: ${bill_to_date:.2f}")
        menu()
        choice = input(">>> ").lower()


def menu():
    print("q)uit, c)hoose taxi, d)rive")


main()
