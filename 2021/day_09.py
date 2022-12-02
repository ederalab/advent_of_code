import numpy as np

def smokeBasins(puzzle_input):
    low_points = []
    tmp = {}  # row : index -> number = row[index]
    basins = {}

    for row in puzzle_input:
        #print(row)
        row = row.replace("\n", "")
        indexes = []
        basins_indexes = []
        for i in range(len(row)-1):
            if i == 0:
                if row[i + 1] > row[i]:
                    indexes.append(i)
            if i < len(row) - 1:
                if row[i + 1] > row[i] and row[i] < row[i - 1]:
                    indexes.append(i)
            if i == len(row) - 1:
                if row[i] < row[i - 1]:
                    indexes.append(i)
            if row[i] != "9":
                basins_indexes.append(i)

        tmp.update({row: indexes})
        basins.update({row: basins_indexes})

    for i in range(len(puzzle_input)):
        for l in tmp[str(puzzle_input[i].replace("\n", ""))]:
            if i == 0:
                if puzzle_input[i+1][l] > puzzle_input[i][l]:
                    low_points.append(int(puzzle_input[i][l]))
            elif i == len(puzzle_input) - 1:
                if puzzle_input[i-1][l] > puzzle_input[i][l]:
                    low_points.append(int(puzzle_input[i][l]))
            else:
                if puzzle_input[i+1][l] > puzzle_input[i][l] and puzzle_input[i-1][l] > puzzle_input[i][l]:
                    low_points.append(int(puzzle_input[i][l]))

    # part 1
    #return sum(low_points) + len(low_points)
    return low_points


if __name__ == '__main__':
    read_input = open('day_09_input.txt', 'r')
    puzzle_input = read_input.readlines()
    #puzzle_input = ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']
    print(smokeBasins(puzzle_input))
