read_input = open('day_04_input.txt', 'r')
line = read_input.readline()

line = line.strip("\n")
first_line = line.split(",")
called_numbers = {}
for (i, el) in enumerate(first_line):
    called_numbers[el] = i+1

boards = []

win_times = []
counter = 0

line = read_input.readline()
while line:
    board = []
    board.append(read_input.readline().strip("\n"))
    board.append(read_input.readline().strip("\n"))
    board.append(read_input.readline().strip("\n"))
    board.append(read_input.readline().strip("\n"))
    board.append(read_input.readline().strip("\n"))

    newBoard = []
    boardOrder = []
    for indx, row in enumerate(board):
        boardOrder.append([])
        newRow = []
        newRow.append(row[0:2].strip(" "))
        boardOrder[indx].append(called_numbers[row[0:2].strip(" ")])
        newRow.append(row[3:5].strip(" "))
        boardOrder[indx].append(called_numbers[row[3:5].strip(" ")])
        newRow.append(row[6:8].strip(" "))
        boardOrder[indx].append(called_numbers[row[6:8].strip(" ")])
        newRow.append(row[9:11].strip(" "))
        boardOrder[indx].append(called_numbers[row[9:11].strip(" ")])
        newRow.append(row[12:14].strip(" "))
        boardOrder[indx].append(called_numbers[row[12:14].strip(" ")])
        newBoard.append(newRow)
    boards.append(newBoard)

    win_time = {}
    # calculating win time required for each row
    for indx, row in enumerate(boardOrder):
        win_time["row" + str(indx)] = max(row)

    # calculating win time required for each column
    for i in range(5):
        column = []
        for j in range(5):
            column.append(boardOrder[j][i])
        win_time["col" + str(i)] = max(column)

    # calculating win time required for first win
    firstWinTime = min(win_time.values())
    win_time["first win"] = firstWinTime

    win_times.append({("board " + str(counter)): win_time})
    # print(win_time,counter)
    counter += 1
    line = read_input.readline()



# calculating winning board
tempArr = []
counter = 0
for wintime in win_times:
    tempArr.append(wintime["board "+str(counter)]["first win"])
    counter += 1

# game 1
# winning_board = (tempArr.index(min(tempArr)))
# game 2
winning_board = (tempArr.index(max(tempArr)))

winning_time = (win_times[winning_board]
               ["board "+str(winning_board)]["first win"])
final_score = 0
for i in range(len(boards[winning_board])):
    for j in range(len(boards[winning_board][i])):
        if(called_numbers[str(boards[winning_board][i][j])] > winning_time):
            final_score += int(boards[winning_board][i][j])


final_score *= int(list(called_numbers.keys())[winning_time-1])
print(final_score)
# 49686 #4512
