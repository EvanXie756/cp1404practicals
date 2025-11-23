from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100)

    distance_driven = my_taxi.drive(40)
    my_taxi.current_fare_distance += distance_driven

    print(f"{my_taxi.name}, fuel={my_taxi.fuel}, odometer={my_taxi.odometer}")
    print("Current fare:", my_taxi.current_fare_distance)

    my_taxi.current_fare_distance = 0

    distance_driven = my_taxi.drive(100)
    my_taxi.current_fare_distance += distance_driven

    print(f"{my_taxi.name}, fuel={my_taxi.fuel}, odometer={my_taxi.odometer}")
    print("Current fare:", my_taxi.current_fare_distance)


main()
