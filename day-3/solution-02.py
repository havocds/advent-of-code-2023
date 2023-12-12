import re
from dataclasses import dataclass
from itertools import product

INPUT_FILE = "./input.txt"
DIGITS_OR_STAR = r"\d+|\*"
ADJACENT_POSITIONS = [-1, 0, 1]
SYMBOL = "*"


@dataclass(frozen=True)
class Match:
    text: str
    row: int
    start: int
    end: int


def read_input(path) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def has_adjacents(mult, num) -> bool:
    if (mult.row - num.row in ADJACENT_POSITIONS) and (
        mult.start - num.start in ADJACENT_POSITIONS
        or mult.end - num.end in ADJACENT_POSITIONS
    ):
        return True
    else:
        return False


def main():
    _sum = 0
    matches = list()
    adjacents = dict()
    lines = read_input(INPUT_FILE)

    for row, line in enumerate(lines):
        matched_items = re.finditer(DIGITS_OR_STAR, line)

        for item in matched_items:
            matches.append(Match(item.group(), row, item.start(), item.end()))

    stars = [m for m in matches if m.text == SYMBOL]
    nums = [m for m in matches if m.text != SYMBOL]

    for star, num in product(stars, nums):
        if has_adjacents(star, num):
            adjacents.setdefault(star, []).append(num)

    for star, num in adjacents.items():
        if len(num) > 1:
            _sum += int(num[0].text) * int(num[1].text)

    print(_sum)


if __name__ == "__main__":
    main()
