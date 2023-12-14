import re

REGEX_PATTERN = r"\d"
NUMBER_MAP = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

INPUT_FILE = "./input.txt"


def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def main():
    sum = 0

    lines = read_input(INPUT_FILE)

    for line in lines:
        callibration = 0

        # lookahead
        matches = re.findall(r"(?=(" + "|".join(NUMBER_MAP.keys()) + r"))", line)

        # now get values from dict
        digits = [NUMBER_MAP.get(c) for c in matches]

        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            callibration = int(f"{first_digit}{last_digit}")

        sum += callibration

    print(sum)


if __name__ == "__main__":
    main()
