from os import readlink, truncate
nums = []
boards = []
drawNums = []
def build_board(line):
    boardss = []
    boardss.extend( #Append the list of numbers to the result array
            [int(item) #Convert each number to an integer
             for item in line.split() #Split each line of whitespace
             ])
    #print(boardss)
    return boardss

    
    
def check(board, num):
    #print(num)
    for line in board:
        bingo = True
        for entry in line:
            if entry not in drawNums: bingo = False;
        if bingo: return winner(board, num)
    for i in range(5):
        bingo = True
        for j in range(5):
            if board[j][i] not in drawNums: bingo = False;
        if bingo: return winner(board, num)
def winner(board, nums):
    sum1 = 0
    for line in board:
        for entry in line:
            if entry not in nums: sum1 += int(entry)
    # print(sum1)
    return sum1
with open('input.txt') as my_file:
    firstline = my_file.readline()
    nums = firstline.rstrip("\n").split(',')
    #print(nums)
    counter = 0
    while True:
        line = my_file.readline()
        if (line == ''): break
        if line != '\n':
            newL = []
            newL.append(build_board(line))
            for i in range(4):
                line = my_file.readline()
                newL.append(build_board(line))
            boards.append(newL)
            counter+=1
        #print(boards)
    for num in nums:
        #print(num)
        for board in boards:
            drawNums.append(int(num))
            ret = check(board, drawNums)
            if ret != None and len(boards) != 1: boards.remove(board)
            elif (ret != None): print(int(ret) * int(num));
        