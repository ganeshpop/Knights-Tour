import Print
def KnightsTour(board,loc):
    





def getPossibilities(board,loc):
    print("The Possible Locations: ")
    count = 0
    for offset1 in [2, -2, 2, -2]:
        for offset2 in [1, -1]:
            count +=1
            if count < 5:
                newLoc = ((loc[0]+offset1),(loc[1]+offset2))
                if inBoard(newLoc):
                    print(newLoc)
                    board[newLoc[0]][newLoc[1]] = "xx"
            else:
                newLoc = ((loc[0]+offset2),(loc[1]+offset1))
                if inBoard(newLoc):
                    print(newLoc)
                    board[newLoc[0]][newLoc[1]] = "xx"


def inBoard(loc):
    if loc[0] >=0 and loc[0] <=7 and loc[1] >= 0 and loc[1] <=7:
        return True
    else:
        return False


board =[[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
KnightsTour(board,(0,0))
'''
for row in range(0,8):
    for column in range(0,8):
        board =[[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
        board[row][column] = "Kn"
        getPossibilities(board,(row,column))
        Print.printBoard(board,"")
'''