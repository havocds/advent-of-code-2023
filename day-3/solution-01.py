import re

# this pattern returns true when only dots and digits found
PATTERN = r'^[.\d]+$'

sum = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line_index, curr_line in enumerate(lines):
        curr_line = ''.join(curr_line)
        digit_start_pos = None
        digit_end_pos = None

        if line_index == 0:
            prev_line = curr_line
        if line_index >= len(lines)-1:
            next_line = curr_line
        else:
            next_line = lines[line_index+1]
           
        for pos, c in enumerate(curr_line):

            # start of sequence
            if c.isdigit() and digit_start_pos is None:
                digit_start_pos = pos
                digit_end_pos = pos

            # currently in sequence
            elif c.isdigit() and digit_start_pos is not None:
                digit_end_pos = pos

            # end of sequence
            elif not c.isdigit() and digit_start_pos is not None:

                if digit_start_pos > 0:
                    tmp = digit_start_pos - 1
                else:
                    tmp = 0

                # now check for symbols in sequence surroundings, same for prev and next sequence
                if not bool(re.match(PATTERN, curr_line[tmp:digit_end_pos+2])) or \
                   not bool(re.match(PATTERN, prev_line[tmp:digit_end_pos+2])) or \
                   not bool(re.match(PATTERN, next_line[tmp:digit_end_pos+2])):
                    part_number = ''.join(curr_line[digit_start_pos:digit_end_pos+1])
                    sum += int(part_number)
                
                digit_start_pos = None
                digit_end_pos = None

        prev_line = curr_line
    
print(sum)
