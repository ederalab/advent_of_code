def binaryDiagnostic1():
    # check power consumption = gamma * epsilon
    read_input = open('day_03_input.txt', 'r')
    puzzle_input = read_input.readlines()
    count = {}
    for line in puzzle_input:
        i = 0
        for l in line:
            l = l.replace("\n", "")
            if l != "":
                if i not in count.keys():
                    count[i] = []
                else:
                    count[i].append(int(l))
                i += 1

    gamma = ""
    epsilon = ""
    for k in count:
        count_0 = 0
        count_1 = 0

        for v in count[k]:
            if v == 0:
                count_0 += 1
            else:
                count_1 += 1

        if count_0 > count_1:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    power_consumption = (int(gamma, 2)) * (int(epsilon, 2))
    return power_consumption

print(binaryDiagnostic1())


def binaryDiagnostic2():
    read_input = open('day_03_input.txt', 'r')
    puzzle_input = read_input.readlines()

    myinput = []

    for line in puzzle_input:
        line = line.replace("\n", "")
        myinput.append(line)

    oxygen = recursive("oxygen", myinput)
    o = int(oxygen[0], 2)

    co2 = recursive("co2", myinput)
    c = int(co2[0], 2)

    print(o*c)


def recursive(rating, l, i=0):
    if len(l) == 1:
        return l

    nl = []
    count_1 = 0
    count_0 = 0

    n = 0
    for line in l:
        if line[i] == "1":
            count_1 += 1
        else:
            count_0 += 1

    if rating == 'oxygen':
        if count_0 <= count_1:
            n = 1
    else:
        if count_0 > count_1:
            n = 1

    for line in l:
        if line[i] == str(n):
            nl.append(line)

    i += 1
    return recursive(rating, nl, i)

print(binaryDiagnostic2())
