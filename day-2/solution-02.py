import re
from enum import Enum
from collections import defaultdict

class Cube(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14

DIGIT_PATTERN = re.compile(r"\b(\d+)\s(?:red|blue|green)\b", re.IGNORECASE)
COLOR_PATTERN = re.compile(r"\b\d+\s(red|blue|green)\b", re.IGNORECASE)

sum = 0
grabs_dict = defaultdict(list)

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:

        if not line.strip(): 
            continue
        
        number_of_cubes = list(map(int, DIGIT_PATTERN.findall(line)))
        cube_colors = list(map(str.lower, COLOR_PATTERN.findall(line)))   
        
        grabs = sorted(set(zip(cube_colors, number_of_cubes)))
        
        for key, value in grabs:
            grabs_dict[key].append(value)
        
        power_of_grab = \
            grabs_dict.get(Cube.RED.name.lower())[-1] * \
            grabs_dict.get(Cube.GREEN.name.lower())[-1] * \
            grabs_dict.get(Cube.BLUE.name.lower())[-1]
        
        sum += power_of_grab

print(sum)
