def printBoard(board,pref):
    border = "+----+----+----+----+----+----+----+----+"
    for row in board:
        print(pref,border)
        cells ="|"
        for cell in row:
            if cell == 0:
                cell = "  "
            elif cell in range(1,10):
                cell = "0{}".format(cell)
            cells +=" {} ".format(cell)
            cells +="|"
                
        print(pref,cells )
    print(pref,border)
