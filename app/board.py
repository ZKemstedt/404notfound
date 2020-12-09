BOARDSIZE = {
    '1': (4, 4),
    '2': (5, 5),
    '3': (8, 8)
}


class Tile:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.explored = False
        self.player = None
        self.monster = None
        self.treasure = None

    def __str__(self) -> str:
        if self.player:
            pass  # TODO
        elif self.explored:
            pass  # TODO
        else:
            return 'X'

    # Not yet sure if this will be a method to Board or Tile.
    def generate_monsters(self) -> None:  # TODO
        pass

    # Not yet sure if this will be a method to Board or Tile.
    def generate_treasures(self) -> None:  # TODO
        pass


class Board:
    def __init__(self, x: int, y: int):
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
