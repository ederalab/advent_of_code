
def sevenSegmentSearch(puzzle_input):
    seven_segments = {'abcefg': 0, 'cf': 1, 'acdeg': 2, 'acdfg': 3, 'bcdf':4, 'abdfg': 5, 'abdefg': 6, 'acf': 7, 'abcdefg': 8, 'abcdfg': 9}

    sorted_segments = sorted(list(dict.fromkeys(seven_segments)), key=len)
    unique_elements = sorted_segments.copy()
    for i in range(len(sorted_segments)):
        if i < len(sorted_segments)-1:
            if len(sorted_segments[i]) == len(sorted_segments[i + 1]):
                if sorted_segments[i] in unique_elements:
                    unique_elements.remove(sorted_segments[i])
                if sorted_segments[i+1] in unique_elements:
                    unique_elements.remove(sorted_segments[i+1])

    unique_len = [len(x) for x in unique_elements]
    newinput = [d.replace("\n", "").split(" | ") for d in puzzle_input]

    digits = 0
    for i in newinput:
        for d in i[1].split(" "):
            if len(d) in unique_len:
                digits += 1

    #return digits

    # part 2 #
    """
    letters = ["a","b","c","d","e","f","g"]
    segments_length = {6: 0, 2: 1, 5: 2, 5: 3, 4:4, 5: 5, 6: 6, 3: 7, 7: 8, 6: 9}
    seven_segments = {1 : str(letters[2]+letters[5])}
    seven_segments.update({7: str(seven_segments[1] + letters[0])})
    seven_segments.update({4: str(seven_segments[1] + letters[1] + letters[3])})
    seven_segments.update({3: str(seven_segments[7] + letters[6] + letters[3])})
    seven_segments.update({0: str(seven_segments[7] + letters[1] + letters[4] + letters[6])})
    seven_segments.update({2: str(seven_segments[3].replace(letters[5], "") + letters[4])})
    seven_segments.update({5: str(seven_segments[3].replace(letters[2], "") + letters[3])})
    seven_segments.update({6: str(seven_segments[5] + letters[4])})
    seven_segments.update({9: str(seven_segments[0].replace(letters[4], "") + letters[3])})
    seven_segments.update({8: str(seven_segments[0] + letters[3])})
    seven_segments = {v: k for k, v in seven_segments.items()}
    """




if __name__ == '__main__':
    #read_input = open('day_08_input.txt', 'r')
    #puzzle_input = read_input.readlines()
    puzzle_input = ['acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf']
    """
    puzzle_input = ['be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
                    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc',
                    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg',
                    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb',
                    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea',
                    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb',
                    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe',
                    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef',
                    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb',
                    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce']
    """
    #print(sevenSegmentSearch(puzzle_input))
    print(sevenSegmentSearch(puzzle_input))

