import re

PATTERN = r"Card\s+(\d+):\s+"
DIGITS = r"\d+"

with open("input.txt") as f:
    lines = f.readlines()

    cards_instances = [1] * len(lines)

    for card_number, line in enumerate(lines, 1):
        digits = re.sub(PATTERN, "", line.strip()).split("|")

        winning_numbers = re.findall(DIGITS, digits[0])
        my_numbers = re.findall(DIGITS, digits[1])

        matching_numbers = set(winning_numbers) & set(my_numbers)
        matching_numbers_count = len(matching_numbers)

        for idx in range(matching_numbers_count):
            cards_instances[card_number + idx] += cards_instances[card_number - 1]

print(sum(cards_instances))
