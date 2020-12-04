class Tiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:
    def __init__(self):
        self.sizex = 0
        self.sizey = 0

    def boardsize(self, x, y):
        for i in range(x):
            for j in range(y):
                tiles = Tiles(i, j)
                self.boardcord.append(tiles)
        global sizex
        global sizey
        sizex = x
        sizey = y

    def board_choice(self):
        diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
        if diffpick == '1':
            self.boardsize(4, 4)
            print("You created a 4x4 board!\n")
        elif diffpick == '2':
            self.boardsize(5, 5)
            print("You created a 5x5 board!\n")
        elif diffpick == '3':
            self.boardsize(8, 8)
            print("You created a 8x8 board!\n")
        else:
            print("Invalid selection")

        print()
