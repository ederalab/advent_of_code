def pilotSubmarine1():
    x = 0 # horizontal position
    y = 0 # depht
    read_input = open('day_02_input.txt', 'r')
    puzzle_input = read_input.readlines()

    for line in puzzle_input:
        l = line.replace("\n", "")
        split_command = l.split(" ")
        c = split_command[0]  # command
        p = int(split_command[1])  # position

        if c == 'forward':
            x  += p
        if c == 'down':
            y += p
        if c == 'up':
            y -= p

    return x * y


print(pilotSubmarine1())


def pilotSubmarine2():
    x = 0 # horizontal position
    y = 0 # depht
    aim = 0
    read_input = open('day_02_input.txt', 'r')
    puzzle_input = read_input.readlines()

    for line in puzzle_input:
        l = line.replace("\n", "")
        split_command = l.split(" ")
        c = split_command[0].lower()  # command
        p = int(split_command[1])  # position

        if c == 'forward':
            x += p
            y += aim * p
        if c == 'down':
            aim += p
        if c == 'up':
            aim -= p
    return x * y

print(pilotSubmarine2())