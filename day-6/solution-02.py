import re

DIGITS = r"\d+"
INPUT_FILE = "./input.txt"


def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f if not line.isspace()]


def main():
    lines = read_input(INPUT_FILE)
    time = int("".join(re.findall(DIGITS, lines[0])))
    record = int("".join(re.findall(DIGITS, lines[1])))

    j = 0
    count = 0
    for i in range(time):
        distance = i * (time - j)

        if distance > record:
            count += 1
        j += 1

    print(count)


if __name__ == "__main__":
    main()
