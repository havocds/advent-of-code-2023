import re

DIGITS = r"\d"

INPUT_FILE = "./input.txt"


def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def main():
    sum = 0

    lines = read_input(INPUT_FILE)

    for line in lines:
        callibration = 0
        digits = re.findall(DIGITS, line)

        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            callibration = int(f"{first_digit}{last_digit}")

        sum += callibration

    print(sum)


if __name__ == "__main__":
    main()
