from typing import Tuple
from app.helpers import user_choice
import random

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
        self.monsters = []
        self.treasure = None
        self.exit = False

    def __str__(self) -> str:
        if self.player:
            return '[P]'
        elif self.explored:
            return '[/]'
        else:
            return '[X]'

    def place_character(self, player):
        self.player = player

    # Not yet sure if this will be a method to Board or Tile.
    def generate_monsters(self) -> None:  # TODO
        pass

    # Not yet sure if this will be a method to Board or Tile.
    def generate_treasures(self) -> None:  # TODO
        pass

    def exit_tile(self) -> bool:
        choices = [
            ('y', 'Leave and save'),
            ('n', 'Stay and explore'),
        ]
        if self.exit:
            print('You found the exit!\n')
            print('Do you want to leave?\n')
            choice = user_choice(choices)
            if choice == 'y':
                return True
            elif choice == 'n':
                # Optional: Add in main game_loop if false, put some marker on this tile (after player moved).
                return False


class Board:
    def __init__(self, x: int, y: int):
        self.sizex = x
        self.sizey = y
        self.tiles = []
        self.generated_exit = False

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
                display_string += f'[ {tile_string} ]  '
            display_string += '\n'

        return (display_string)

    def get_tile(self, coordinates: Tuple[int, int]) -> Tile:
        try:
            x, y = coordinates
            tile = self.tiles[x][y]
        except IndexError:
            return None
        print(f'[Control Flow] [Board] get_tile(({x},{y}))')
        return tile

    def generate_exit_tile(self) -> None:
        if self.generated_exit is False:
            for row in random.sample(self.tiles, 1):
                for tile in random.sample(row, 1):
                    exit_tile = tile
                    exit_tile.exit = True
        else:
            print('The board already has an exit!')


if __name__ == "__main__":
    board = Board(4, 4)
    print(board)

    example_player = ':)'

    tile = board.get_tile((0, 3))
    tile.place_character(example_player)
    print(board)

    target = board.get_tile((1, 3))
    target.place_character(example_player)
    print(board)

