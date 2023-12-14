import re

CARD_PATTERN = r"Card\s+(\d+):\s+"
DIGITS = r"\d+"
INPUT_FILE = "./input.txt"


def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def main():
    points = 0
    lines = read_input(INPUT_FILE)

    for line in lines:
        card_numbers = re.sub(CARD_PATTERN, "", line.strip()).split("|")

        winning_numbers = re.findall(DIGITS, card_numbers[0])
        my_numbers = re.findall(DIGITS, card_numbers[1])
        matching_numbers = set(winning_numbers) & set(my_numbers)
        matching_numbers_count = len(matching_numbers)

        points += (
            2 ** (matching_numbers_count - 1) if matching_numbers_count >= 1 else 0
        )

    print(points)


if __name__ == "__main__":
    main()
