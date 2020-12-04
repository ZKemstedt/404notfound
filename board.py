BOARDSIZE = {
    '1': (4, 4),
    '2': (5, 5),
    '3': (8, 8) 
}


class Tiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        
        return 'X'


class Board:
    def __init__(self, x, y):
        self.sizex = x
        self.sizey = y
        self.tiles = []

        for col in range(x):
            rows = []
            for row in range(y):
                tile = Tiles(col, row)
                rows.append(tile)
            #print(rows)

    





def create_board():
    ask_again = True
    while ask_again:
        
        diffpick = input('Choose boardsize!\n[1] Small\n[2] Medium\n[3] Large\n')
        ask_again = False
        
        if diffpick == '1':
            print("You created a 4x4 board!\n")
        elif diffpick == '2':
            print("You created a 5x5 board!\n")
        elif diffpick == '3':
            print("You created a 8x8 board!\n")
        else:
            ask_again = True
            print("Invalid selection")

    x, y = BOARDSIZE[diffpick]
    board = Board(x, y)
    return board


def displayBoard(board): 
    
    tempstring = ''
    for column in range(board.sizey,0,-1):
    
        for row in range(0,board.sizex):
            
            tile = board.tiles
            tile_string = str(tile)
            
                      
            tempstring += f'{tile_string}   '
        tempstring += '\n'
        
                
    return (tempstring)

print(displayBoard(Board(4,4)))
