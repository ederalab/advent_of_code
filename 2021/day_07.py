def theTreacheryOfWhales(puzzle_input):

    newinput = [int(d) for d in puzzle_input[0].split(",")]
    #print(newinput, "\n")
    fuel = []
    for n in range(len(newinput)):
        shift = [abs(num-n) for num in newinput]
        total_shift = sum(shift)
        fuel.append(total_shift)

    return min(fuel)


def theTreacheryOfWhales2(puzzle_input):

    newinput = [int(d) for d in puzzle_input[0].split(",")]

    fuel = []

    for n in range(len(newinput)):
        shift = [abs(num - n) for num in newinput]
        total_shift = sum([sum(list(range(s + 1))) for s in shift])

        fuel.append(total_shift)

    return min(fuel)


if __name__ == '__main__':
    read_input = open('day_07_input.txt', 'r')
    puzzle_input = read_input.readlines()
    #puzzle_input = ["16,1,2,0,4,2,7,1,2,14"]
    #print(theTreacheryOfWhales(puzzle_input))
    print(theTreacheryOfWhales2(puzzle_input))

