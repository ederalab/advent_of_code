def dumboOctopus(puzzle_input):
    steps = 2
    s = 0
    while s <= steps:
        a = [int(puzzle_input[x][y]) for x in range(len(puzzle_input)) for y in range(len(puzzle_input[x])) if puzzle_input[x][y] != '\n']
        print(a)
        s += 1


#def flashes:


if __name__ == '__main__':
    read_input = open('day_11_input.txt', 'r')
    #puzzle_input = read_input.readlines()
    puzzle_input = ["11111\n", "19991\n", "19191\n", "19991\n", "11111\n"]
    print(dumboOctopus(puzzle_input))
