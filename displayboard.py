board = [[1,2,3],[4,5,6],[7,8,9]]



def displayBoard(board):    #insert xx 2d array and return 
    tempstring = ''
    columns = len(board[0])
    row = len(board)
    
    for i in range(columns,0,-1):
        for j in range(row):
            tempstring += 'X' + ' '
            if(j == row - 1):
                tempstring += '\n'
                
                
    return tempstring

displayBoard(board)