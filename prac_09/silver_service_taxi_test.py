from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test taxi", 100, 2)

    taxi.current_fare_distance()
    taxi.drive(100)

    fare = taxi.get_fare()
    print(f"Calculated fare: {fare:.2f}")



main()
