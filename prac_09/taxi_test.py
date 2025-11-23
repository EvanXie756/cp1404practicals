from prac_09.taxi import Taxi


def main():
    my_taxi = Taxi("Prius 1", 100, 1.23)

    distance_driven = my_taxi.drive(40)
    my_taxi.current_fare_distance += distance_driven



main()
