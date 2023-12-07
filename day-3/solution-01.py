import re

# this pattern returns true when only dots and digits found
PATTERN = r'^[.\d]+$'

sum = 0

with open("input.txt") as f:
    lines = f.readlines()

    for line_index, current_line in enumerate(lines):
        current_line_list = ''.join(current_line)
        digit_start_pos = None
        digit_end_pos = None

        if line_index == 0:
            prev_line_list = current_line_list
        if line_index >= len(lines)-1:
            next_line_list = None
        else:
            next_line_list = lines[line_index+1]

        if next_line_list is None:
            next_line_list = current_line_list
            
        for pos, c in enumerate(current_line_list):

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
                    start_seq = digit_start_pos - 1
                else:
                    start_seq = 0

                # now check for symbols in sequence surroundings, same for prev and next sequence
                if not bool(re.match(PATTERN, current_line_list[start_seq:digit_end_pos+2])) or \
                   not bool(re.match(PATTERN, prev_line_list[start_seq:digit_end_pos+2])) or \
                   not bool(re.match(PATTERN, next_line_list[start_seq:digit_end_pos+2])):
                    part_number = ''.join(current_line_list[digit_start_pos:digit_end_pos+1])
                    sum += int(part_number)
                
                digit_start_pos = None
                digit_end_pos = None

        prev_line_list = current_line_list
    
print(sum)
