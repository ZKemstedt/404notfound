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


if __name__ == "__main__":
    print(display_board(Board(4, 4)))
