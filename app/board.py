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

    def __str__(self) -> str:
        display_string = ''
        for column in range(self.sizey, 0, -1):
            for row in range(0, self.sizex):
                tile = self.tiles[row][column-1]
                tile_string = str(tile)
                display_string += f'{tile_string}   '
            display_string += '\n'

        return (display_string)

    def get_tile() -> Tile:
        pass


if __name__ == "__main__":
    board = Board(4, 4)
    print(board)
