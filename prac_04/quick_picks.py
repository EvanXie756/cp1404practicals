import random

LOW_NUMBER = 1
HIGHEST_NUMBER = 45
NUMBERS_PER_PICK = 6

number_of_picks = int(input("How many quick picks? "))
for i in range(number_of_picks):
    quick_picks = []
    while len(quick_picks) < NUMBERS_PER_PICK:
        number = random.randint(LOW_NUMBER, HIGHEST_NUMBER)
        if number not in quick_picks:
            quick_picks.append(number)
    quick_picks.sort()
    print(' '.join(f"{i:2}" for i in quick_picks))

