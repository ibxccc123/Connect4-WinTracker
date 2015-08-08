__author__ = 'Danny Peng'

#X in Grid Represents Player X
#O in Grid Represents Player O
def decideWinner(input):
    grid = [] #Empty List
    counter = 0
    for row in range(6):
        grid.append([]) #Appends an empty list (six times) to grid[]
        for column in range(7): #In each of those empty lists in grid[], appends 7 '0's
            grid[row].append('-')
    with open(input, 'r') as fileIn:
        while True:
            str = fileIn.read(1) #reads in file one character at a time
            if not str:
                break
            elif not str.isspace(): #If the column placement is not an empty whitespace string that has at least one character in it
                if enterGrid(str, grid, counter):  #modifies the grid with the piece of the player using the info of
                    break #breaks if there is a winner
                # the column they placed their piece along with who they are
                # (counter % 2 == 0 is the first player, otherwise the second player)
                counter = counter + 1 #increases the move counter by one

def enterGrid(str, grid, counter):  #modifies the grid that is kept within the file-reading loop in decideWinner()
    print(counter)
    if counter % 2 == 0:
        player = 'X'
    else:
        player = 'Y'
    #translates the column input into the list index
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
    #checks each column's row to see if a piece has been placed, starting from the 0th row
    for row in range(6):
        if grid[row][column] is '-':
            grid[row][column] = player
            print(grid)
            piece = victoryCheck(grid, row, column) #checks to see if Player X or O has won yet
            if piece == 'X' or piece == 'O':
                print("Player " + piece + " has won at turn ",  (counter + 1))
                return 1
            break #otherwise, breaks out after placing down the player's piece in its rightful column/row and returns back to decideWinner()

def victoryCheck(grid, row, column):
    piece = grid[row][column]

    return piece

def main():
    decideWinner('input.txt') #Extracts the winner from an input.txt
main() #runs main()
