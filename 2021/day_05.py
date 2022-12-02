import re

def hydrothermal_venture():
    # x1,y1 -> x2,y2
    read_input = open('day_05_input.txt', 'r')
    puzzle_input = read_input.readlines()

    coordinates = {}
    matrix = {}
    i = 0
    maxnum = []

    for line in puzzle_input:
        line = line.strip("\n")
        split_coords = re.split('[->\, ]', line)
        s = list(filter(None, split_coords))
        coordinates[i] = [[s[0], s[1]],[s[2], s[3]]]
        maxnum.append(s[0])
        maxnum.append(s[1])
        maxnum.append(s[2])
        maxnum.append(s[3])
        i += 1

    maxnum = sorted(maxnum)
    maxnum = int(maxnum[-1]) + 1

    for n in range(maxnum):
        matrix[n] = ["."] * maxnum

    lines = []
    for c in coordinates.values():
        # part 1 # horizontal and vertical #
        # if c[0][0] == c[1][0] or c[0][1] == c[1][1]:
        #   lines.append(c)
        # part 2 # diagonal #
        lines.append(c)

    for [[x1, y1], [x2, y2]] in lines:
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int(y2)

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if matrix[y][x1] == ".":
                    matrix[y][x1] = 1
                else:
                    matrix[y][x1] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                if matrix[y1][x] == ".":
                    matrix[y1][x] = 1
                else:
                    matrix[y1][x] += 1
        if abs(x2 - x1) == abs(y2 - y1):
            mn = [x1, y1] if y1 < y2 else [x2, y2]
            mx = [x2, y2] if y1 < y2 else [x1, y1]
            dir = 1 if mn[0] < mx[0] else -1
            if mn[0] < mx[0]:
                for i, x in enumerate(range(mn[0], mx[0] + 1)):
                    if matrix[mn[1] + i][x] == ".":
                        matrix[mn[1] + i][x] = 1
                    else:
                        matrix[mn[1] + i][x] += 1
            else:
                for i, x in enumerate(range(mn[0], mx[0] - 1, -1)):
                    if matrix[mn[1] + i][x] == ".":
                        matrix[mn[1] + i][x] = 1
                    else:
                        matrix[mn[1] + i][x] += 1


    counter = [x for v in matrix.values() for x in v if type(x) == int and x > 1]

    return len(counter)

print(hydrothermal_venture())