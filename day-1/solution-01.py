import re

REGEX_PATTERN = r"\d"
sum = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line in lines:
        callibration = 0
        digits = re.findall(REGEX_PATTERN, line)

        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            callibration = int(f"{first_digit}{last_digit}")

        sum += callibration

print(sum)