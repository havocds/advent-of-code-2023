import re
from enum import Enum

ID_PATTERN = re.compile(r"^\bGame\s(\d+)\b", re.IGNORECASE)
DIGIT_PATTERN = re.compile(r"\b(\d+)\s(?:red|blue|green)\b", re.IGNORECASE)
COLOR_PATTERN = re.compile(r"\b\d+\s(red|blue|green)\b", re.IGNORECASE)

INPUT_FILE = "./input.txt"


class Cube(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14
    MAX = 15


def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f]


def main():
    sum = 0
    lines = read_input(INPUT_FILE)

    for line in lines:
        if not line.strip():
            continue

        number_of_cubes = list(map(int, DIGIT_PATTERN.findall(line)))

        if sorted(number_of_cubes, reverse=True)[0] >= Cube.MAX.value:
            continue

        id = int(ID_PATTERN.findall(line)[0])

        cube_colors = list(map(str.lower, COLOR_PATTERN.findall(line)))
        grabs = sorted(set(zip(number_of_cubes, cube_colors)), reverse=True)

        for grab in grabs:
            if grab[1] == Cube.RED.name.lower() and grab[0] > Cube.RED.value:
                valid_grab = False
                break
            elif grab[1] == Cube.GREEN.name.lower() and grab[0] > Cube.GREEN.value:
                valid_grab = False
                break
            elif grab[1] == Cube.BLUE.name.lower() and grab[0] > Cube.BLUE.value:
                valid_grab = False
                break
            else:
                valid_grab = True

        if valid_grab:
            sum += id

    print(sum)


if __name__ == "__main__":
    main()
