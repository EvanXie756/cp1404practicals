"""
Wimbledon
Estimate: 25 minutes
Actual:   50 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    records = read_wimbledon_data(FILENAME)
    champion_wins = count_champion_wins(records)
    countries = extract_countries(records)
    display_results(champion_wins, countries)


def read_wimbledon_data(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        records = []
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def count_champion_wins(records):
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def extract_countries(records):
    countries = {record[1] for record in records}
    return countries


def display_results(champion_to_wins, countries):
    print("Wimbledon Champions")
    for champion, wins in champion_to_wins.items():
        print(f"{champion:20} {wins}")
    print()
    sorted_champions = sorted(countries)
    print(f"These {len(sorted_champions)} countries have won Wimbledon:")
    print(", ".join(countries))


main()
