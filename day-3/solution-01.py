import re
from typing import Final

INPUT_FILE: Final = "./test_input.txt"
DIGITS: Final = r"\d+"


def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def is_symbol(char: str) -> bool:
    return char != "." and not char.isdigit()


def main() -> None:
    _sum: int = 0
    lines = read_input(INPUT_FILE)

    for row, line in enumerate(lines):
        matched_items = re.finditer(DIGITS, line)

        for item in matched_items:
            start_index = item.start() - 1
            end_index = item.end()
            number = int(item.group())

            if (start_index >= 0 and is_symbol(line[start_index])) or (
                end_index < len(line) and is_symbol(line[end_index])
            ):
                _sum += number
                continue

            for i in range(start_index, end_index + 1):
                if i >= len(line):
                    continue
                if (i > 0 and is_symbol(lines[row - 1][i])) or (
                    i < len(lines) - 2 and is_symbol(lines[row + 1][i])
                ):
                    _sum += number
                    break

    print(_sum)


if __name__ == "__main__":
    main()
