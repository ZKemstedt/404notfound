from typing import Tuple
from helpers import user_choice
from monster import GiantSpider, Skeleton, Orc, Troll
from treasure import Coins, Pouch, GoldJewelry, Gemstone, SmallTreasureChest
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
        self.treasures = []
        self.exit = False

    def __str__(self) -> str:
        tile_format = ' [ {} ] '
        if self.player:
            string = 'P'
        elif self.explored:
            string = '/'
        else:
            string = 'X'
        return tile_format.format(string)

    def place_character(self, player):
        self.player = player

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
        self.generated_monsters = False
        self.generated_treasures = False

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
                display_string += f'{tile_string}'
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
            self.generated_exit = True
        else:
            print('The board already has an exit!')

    def generate_monster(self) -> None:
        monster_list = {'Giantspider': 20, 'Skeleton': 15, 'Orc': 10, 'Troll': 5}
        if self.generated_monsters is False:
            for row in self.tiles:
                for tile in row:
                    for item in monster_list:
                        random_roll = random.randint(0, 100)
                        monster_percent = monster_list.get(item)
                        if random_roll <= monster_percent:
                            tile.monsters.append(item)
                            print(tile.monsters)
            self.generated_monsters = True
        else:
            print('The board already has monsters!')

    def generate_treasure(self) -> None:
        treasure_list = {'Coins': 40, 'Pouch': 20, 'GoldJewelry': 15, 'Gemstone': 10, 'SmallTreasureChest': 5}
        if self.generated_treasures is False:
            for row in self.tiles:
                for tile in row:
                    for item in treasure_list:
                        random_roll = random.randint(0, 100)
                        treasure_percent = treasure_list.get(item)
                        if random_roll <= treasure_percent:
                            if item == 'Coins':
                                tile.treasures.append(Coins())
                            elif item == 'Pouch':
                                tile.treasures.append(Pouch())
                            elif item == 'GoldJewelry':
                                tile.treasures.append(GoldJewelry())
                            elif item == 'Gemstone':
                                tile.treasures.append(Gemstone())
                            elif item == 'SmallTreasureChest':
                                tile.treasures.append(SmallTreasureChest())
            self.generated_treasures = True
        else:
            print('The board already has treasures!')


if __name__ == "__main__":
    board = Board(4, 4)
    print(board)

    board.generate_monster()
    board.generate_treasure()
