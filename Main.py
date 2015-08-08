__author__ = 'Penguin'

def analyzeGrid(str, grid, checker):
    print(checker)
    if checker % 2 == 0:
        player = 'X'
    else:
        player = 'Y'
    if str == 'a' or str == 'A':
        column = 0
    if str == 'b' or str == 'B':
        column = 1
    if str == 'c' or str == 'C':
        column = 2
    if str == 'd' or str == 'D':
        column = 3
    if str == 'e' or str == 'E':
        column = 4
    if str == 'f' or str == 'F':
        column = 5
    if str == 'g' or str == 'G':
        column = 6
    for num in range(6):
        if grid[num][column] is '-':
            grid[num][column] = player
            print(grid)
            break

#X in Grid Represents Player X
#O in Grid Represents Player O
def decideWinner(input):
    grid = [] #Empty List
    checker = 0
    for row in range(6):
        grid.append([]) #Appends an empty list (six times) to grid[]
        for column in range(7): #In each of those empty lists in grid[], appends 7 '0's
            grid[row].append('-')
    with open(input, 'r') as fileIn:
        while True:
            str = fileIn.read(1)
            if not str:
                break
            elif not str.isspace(): #If str is not an empty whitespace string that has at least one character in it
                analyzeGrid(str, grid, checker)
                checker = checker + 1


def main():
    decideWinner('input.txt')
main()
