MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""


def main():
    print(MENU)
    menu = input("Choice: ").upper()
    while menu != "q":
        if menu == "g":
            score = get_valid_score()


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "bad"

def get_valid_score():
    


main()
