def countMeasurements1(puzzle_input):
    count = 0

    first = puzzle_input[0]
    n = int(first.replace("\n", ""))

    for line in puzzle_input:
        num = int(line.replace("\n", ""))
        if num < n:
            count += 1
        n = num

    return count


def countMeasurements2(puzzle_input):
    count = 0

    num = int(puzzle_input[0].replace("\n", "")) + int(puzzle_input[1].replace("\n", "")) + int(puzzle_input[2].replace("\n", ""))
    n = num
    for i in range(len(puzzle_input)-2):
        s = int(puzzle_input[i].replace("\n", "")) + int(puzzle_input[i+1].replace("\n", "")) + int(puzzle_input[i+2].replace("\n", ""))
        #print(s)
        if s > n:
            count += 1
        n = s

    return count


if __name__ == '__main__':
    read_input = open('day_01_input.txt', 'r')
    puzzle_input = read_input.readlines()
    print(countMeasurements1(puzzle_input))
    print(countMeasurements2(puzzle_input))
