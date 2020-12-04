BOARDSIZE = {
    '1': (4, 4),
    '2': (5, 5),
    '3': (8, 8) 
}


class Tiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y


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
            print(rows)




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
