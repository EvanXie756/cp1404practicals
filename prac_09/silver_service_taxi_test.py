from silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test taxi", 100, 2)

    taxi.drive(18)

    fare = taxi.get_fare()
    print(f"Calculated fare: {fare:.2f}")

    expected_fare = 48.78
    assert fare == expected_fare, f"Fare should be {expected_fare}, got {fare}"


main()
