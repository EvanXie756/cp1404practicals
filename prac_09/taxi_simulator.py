from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    print("Let's drive")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("limo", 100, 2),
             SilverServiceTaxi("Truck", 200, 4)]


main()
