def lanternfish():
    read_input = open('day_06_input.txt', 'r')
    puzzle_input = read_input.readlines()

    i = 1
    for line in puzzle_input:
        line = line.strip("\n")
        lanternfishes = line.split(",")

    occurrences = [0] * 9

    for lf in lanternfishes:
        occurrences[int(lf)] += 1

    days = 256
    for day in range(1, days+1):
        tmp = occurrences[0]
        for i in range(0, len(occurrences)-1):
            occurrences[i] = occurrences[i+1]
        occurrences[8] = tmp
        occurrences[6] += tmp

    return sum(occurrences)


print(lanternfish())