import re

PATTERN = r"Card\s+(\d+):\s+"
DIGITS = r"\d+"

points = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        card_numbers = re.sub(PATTERN, "", line.strip()).split("|")

        winning_numbers = re.findall(DIGITS, card_numbers[0])
        my_numbers = re.findall(DIGITS, card_numbers[1])
        matching_numbers = set(winning_numbers) & set(my_numbers)
        matching_numbers_count = len(matching_numbers)

        points += 2 ** (matching_numbers_count - 1) if matching_numbers_count >= 1 else 0

print(points)
