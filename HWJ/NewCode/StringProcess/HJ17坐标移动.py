"""

"""

import sys

for line in sys.stdin:
    input_lst = line.split()
    print(input_lst)

    for ele in input_lst:
        move_coordinate_lst = ele.split(";")
        x, y = 0, 0
        for move_coordinate in move_coordinate_lst:
            if len(move_coordinate) < 2 or len(move_coordinate) > 10000:
                continue
            try:
                step = int(move_coordinate[1:])
            except ValueError:
                continue
            direction = move_coordinate[0]

            if direction == "A":
                x -= step
            elif direction == "D":
                x += step
            elif direction == "S":
                y -= step
            elif direction == "W":
                y += step

        print(f"{x},{y}")
