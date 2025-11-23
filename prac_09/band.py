class band:

    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        musicians_string = ",".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_string})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            if musician.instruments:
                print(f"{musician.name} is playing: {musician.instruments[0]}")
            else:
                print(f"{musician.name} needs and instrument")
