import re

PATTERN = r"\d+"


def go_forwards(line, start=0):
    part_number = ""
    for c in line[start:]:
        if c.isdigit():
            part_number = part_number + c
        else:
            break
    return part_number


def go_backwards(line, end=0):
    part_number = ""
    for c in reversed(line[:end]):
        if c.isdigit():
            part_number = part_number + c
        else:
            break
    return part_number[::-1]


with open("input.txt") as f:
    lines = f.readlines()

    sum = 0

    for line_index, curr_line in enumerate(lines):
        curr_line = "".join(curr_line.strip())

        if line_index == 0:
            prev_line = curr_line
        if line_index >= len(lines) - 1:
            next_line = curr_line
        else:
            next_line = lines[line_index + 1]

        for pos, c in enumerate(curr_line):
            if c == "*":
                adjacents = 0

                # check number of adjacents before doing anything
                if curr_line[pos - 1].isdigit():
                    adjacents += 1
                if curr_line[pos + 1].isdigit():
                    adjacents += 1
                adjacents += len(re.findall(PATTERN, prev_line[pos - 1:pos + 2]))
                adjacents += len(re.findall(PATTERN, next_line[pos - 1:pos + 2]))

                if adjacents != 2:
                    continue

                part_numbers = list()

                # part numbers next to *
                if curr_line[pos - 1].isdigit():
                    part_numbers.append(go_backwards(curr_line, end=pos))
                if curr_line[pos + 1].isdigit():
                    part_numbers.append(go_forwards(curr_line, start=pos + 1))

                # part number in prev line at * position
                if prev_line[pos].isdigit():
                    part_numbers.append(
                        go_backwards(prev_line, end=pos + 1)
                        + go_forwards(prev_line, start=pos + 1)
                    )
                # part number in prev line at position -1 or +1 of *
                else:
                    if prev_line[pos - 1].isdigit():
                        part_numbers.append(go_backwards(prev_line, end=pos))
                    if prev_line[pos + 1].isdigit():
                        part_numbers.append(go_forwards(prev_line, start=pos + 1))

                # part number in next line at * position
                if next_line[pos].isdigit():
                    part_numbers.append(
                        go_backwards(next_line, end=pos + 1)
                        + go_forwards(next_line, start=pos + 1)
                    )
                # part number in next line at position -1 or +1 of *
                else:
                    if next_line[pos - 1].isdigit():
                        part_numbers.append(go_backwards(next_line, end=pos))
                    if next_line[pos + 1].isdigit():
                        part_numbers.append(go_forwards(next_line, start=pos + 1))

                sum += int(part_numbers[0]) * int(part_numbers[1])

        prev_line = curr_line

print(sum)
