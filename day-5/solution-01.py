import re
from typing import List

DIGITS = r"\d+"
INPUT_FILE = "./input.txt"


def read_input(path: str) -> list:
    with open(path) as f:
        return [line.strip() for line in f if not line.isspace()]


def create_maps(lines: list) -> List[dict]:
    maps = list()

    for line in lines[1:]:
        if "map" in line:
            maps.append(dict())
        else:
            destination, source, length = map(int, re.findall(DIGITS, line))
            maps[-1][range(source, source + length)] = range(
                destination, destination + length
            )
    return maps


def lookup_location(seed: int, maps: List[dict]) -> int:
    value = seed

    for current_map in maps:
        value = next(
            (
                destination_range.start + (value - source_range.start)
                for source_range, destination_range in current_map.items()
                if value in source_range
            ),
            value,
        )
    return value


def main():
    lines = read_input(INPUT_FILE)
    seeds = [int(seed) for seed in re.findall(DIGITS, lines[0])]
    maps = create_maps(lines)

    locations = [lookup_location(seed, maps) for seed in seeds]
    print(min(locations))


if __name__ == "__main__":
    main()
