from statistics import median

def syntaxScoring(puzzle_input):
    """
    # PART 1 ignore the incomplete lines - just consider the corrupted
    ): 3 points ]: 57 points }: 1197 points >: 25137 points
    # PART 2 complete the incomplete lines
    ): 1 point ]: 2 points }: 3 points >: 4 points
    """
    symbols = {")":"(", "]":"[", "}":"{", ">":"<"}
    points = {")": 3, "]": 57, "}": 1197, ">": 25137, "(": 1, "[": 2, "{": 3, "<": 4}

    total_points = 0
    final_score = []

    for line in puzzle_input:
        line = line.replace("\n", "")
        stack = []
        p2points = 0  # multiply by 5 + value

        for c in line:
            if c in symbols:
                open = stack.pop()
                if open != symbols[c]:
                    total_points += points[c]
                    break
            else:
                stack.append(c)
        else:
            while stack:
                #print(p2points, points[stack.pop()])
                p2points = p2points * 5 + points[stack.pop()]
            final_score.append(p2points)

    final = median(final_score)
    #return total_points
    return final



if __name__ == '__main__':
    read_input = open('day_10_input.txt', 'r')
    puzzle_input = read_input.readlines()
    #puzzle_input = ["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>(", "{([(<{}[<>[]}>{[]{[(<()>" , "(((({<>}<{<{<>}{[]{[]{}", "[[<[([]))<([[{}[[()]]]", "[{[{({}]{}}([{[{{{}}([]", "{<[[]]>}<{[{[{[]{()[[[]", "[<(<(<(<{}))><([]([]()", "<{([([[(<>()){}]>(<<{{", "<{([{{}}[<[[[<>{}]]]>[]]"]
    print(syntaxScoring(puzzle_input))
