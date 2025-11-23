from prac_09.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super.__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_chance = random.random(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0