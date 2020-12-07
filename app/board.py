BOARDSIZE = {
    '1': (4, 4),
    '2': (5, 5),
    '3': (8, 8)
}


class Tile:
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
                tile = Tile(col, row)
                rows.append(tile)
                self.tiles.append(rows)
            # print(rows)


def choose_board_size():
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


def display_board(board):

    display_string = ''
    for column in range(board.sizey, 0, -1):
        for row in range(0, board.sizex):
            tile = board.tiles[row][column-1]
            tile_string = str(tile)
            display_string += f'{tile_string}   '

        if(row != board.sizex and (column != 1)):
            display_string += '\n'

    return (display_string)


def choose_start_position(board):
    choose_position = input("Choose from where you want to start game:\n 1.Top left \n 2.Top right \n 3.Bottom left \n 4.Bottom right")

    if choose_position == "1":
        start_pos_x = 0
        start_pos_y = 0
        start_pos = (start_pos_x, start_pos_y)

    elif choose_position == "2":
        start_pos_x = 0
        start_pos_y = board.sizey - 1
        start_pos = (start_pos_x, start_pos_y)

    elif choose_position == "3":
        start_pos_x = board.sizex - 1
        start_pos_y = 0
        start_pos = (start_pos_x, start_pos_y)

    elif choose_position == "4":
        start_pos_x = board.sizex - 1
        start_pos_y = board.sizey - 1
        start_pos = (start_pos_x, start_pos_y)

    # TODO
    else:
        pass

    return start_pos


if __name__ == "__main__":
    print(displayBoard(Board(4,4)))
