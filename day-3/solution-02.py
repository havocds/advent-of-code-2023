import re

PATTERN2 = r'\d+'
PATTERN5 = r'(\d+)\*(\d+)'
PATTERN6 = r'(\d+)\*'
PATTERN7 = r'\*(\d+)'
PATTERN8 = r'(\d+)'

sum = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line_index, curr_line in enumerate(lines):
        curr_line = ''.join(curr_line)
        adjacents = 0

        if line_index == 0:
            prev_line = curr_line
        if line_index >= len(lines)-1:
            next_line = curr_line
        else:
            next_line = lines[line_index+1]

        for pos, c in enumerate(curr_line):

            if c == "*":
                
                adjacents = 0
                
                if curr_line[pos-1].isdigit():
                    adjacents += 1
                if curr_line[pos+1].isdigit():
                    adjacents += 1
                adjacents += len(re.findall(PATTERN2, prev_line[pos-1:pos+2]))
                adjacents += len(re.findall(PATTERN2, next_line[pos-1:pos+2]))      
                
                if adjacents != 2:
                    continue

                ratios = list()

                star_has_two_neighbours = re.search(PATTERN5, curr_line)
                if star_has_two_neighbours:
                    ratios.append(int(star_has_two_neighbours.group(1)))
                    ratios.append(int(star_has_two_neighbours.group(2)))
                else:
                    if curr_line[pos-1].isdigit():
                        star_has_left_neighbour = re.search(PATTERN6, curr_line[:pos+1])
                        ratios.append(int(star_has_left_neighbour.group(1)))
                    if curr_line[pos+1].isdigit():
                        star_has_right_neighbour = re.search(PATTERN7, curr_line[pos:])
                        ratios.append(int(star_has_right_neighbour.group(1)))

                if re.search(PATTERN8, prev_line) is not None:
                    matches_prev = re.finditer(PATTERN2, prev_line)
                    
                    for match in matches_prev:
                        digits = match.group()
                        if pos == match.start():
                            ratios.append(int(digits))
                            
                        if pos-1 in range(match.start(), match.end()):
                            ratios.append(int(digits))
                            
                        if pos+1 in range(match.start(), match.end()+1):
                            ratios.append(int(digits))
                            

                if re.search(PATTERN8, next_line) is not None:
                    matches_next = re.finditer(PATTERN2, next_line)
                    
                    for match in matches_next:
                        digits = match.group()
                        if pos == match.start():
                            ratios.append(int(digits))
                            
                        if pos-1 in range(match.start(), match.end()):
                            ratios.append(int(digits))
                            
                        if pos+1 in range(match.start(), match.end()+1):
                            ratios.append(int(digits))

                sum += ratios[0] * ratios[1]
                
        prev_line = curr_line

print(sum)
