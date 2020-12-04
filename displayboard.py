from board import Board,Tiles

def displayBoard(board):    #Insert board object and return string 
    
    tempstring = ''
    for column in range(int(board.sizey),0,-1): #Starts topleft
    
        for row in range(0,int(board.sizex)):
            tile = Tiles(row,column-1)
            tile_string = str(tile)
            
                      
            tempstring += f'{tile_string}   '
        tempstring += '\n'
        
                
    return (tempstring)

displayBoard(Board(5,5))
