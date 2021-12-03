def countMeasurements1():
    count = 0
    read_input = open('day_01_input.txt', 'r')
    puzzle_input = read_input.readlines()

    first = puzzle_input[0]
    n = int(first.replace("\n", ""))

    for line in puzzle_input:
        num = int(line.replace("\n", ""))
        if num > n:
            count += 1
        n = num

    return count


print(countMeasurements1())


def countMeasurements2():
    count = 0
    read_input = open('day_01_input.txt', 'r')
    puzzle_input = read_input.readlines()

    num = int(puzzle_input[0].replace("\n", "")) + int(puzzle_input[1].replace("\n", "")) + int(puzzle_input[2].replace("\n", ""))
    n = num
    for i in range(len(puzzle_input)-2):
        s = int(puzzle_input[i].replace("\n", "")) + int(puzzle_input[i+1].replace("\n", "")) + int(puzzle_input[i+2].replace("\n", ""))
        #print(s)
        if s > n:
            count += 1
        n = s

    return count

print(countMeasurements2())
