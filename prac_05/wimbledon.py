"""
CP1404 Practical Wimbledon
"""

FILENAME = "wimbledon.csv"


def main():
    """Display Wimbledon champions and countries."""
    records = load_data(FILENAME)
    champion_to_wins, countries = process_data(records)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read Wimbledon CSV file and return data as list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header
        records = [line.strip().split(",") for line in in_file]
    return records


def process_data(records):
    """Process data into dictionary of champions and set of countries."""
    champion_to_wins = {}
    countries = set()
    for record in records:
        champion = record[2]
        country = record[1]
        countries.add(country)
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins, countries


def display_results(champion_to_wins, countries):
    """Display champions with win counts and countries alphabetically."""
    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_wins.items()):
        print(f"{champion:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
