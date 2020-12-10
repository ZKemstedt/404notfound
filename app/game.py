# Game loop
#
#
#   Run (Loop)
#       -> Display Board
#       -> Move Character
#       -> Pause Game
#
#   Battle code goes in here too
#
#   Exit
#
import random
import time
from typing import List, Union, Tuple

from app.board import Board, Tile
from app.monster import Monster
from app.character import Character
from app.helpers import user_choice


GAME_OVER = """
              _______       ____      ___   ___   _______
             /  ,____\\     /    \\    |   \\_/   | |  ,____|
            |  |  ____    /  /\\  \\   |         | |  |__
            |  | |__  |  /  /__\\  \\  |  |`-´|  | |   __|
            |  |___|  | /  ______  \\ |  |   |  | |  |____
             \\_______/ /__/      \\__\\|  |   |__| |_______|
              _____  ___      ___  _______   _______     __
             /  _  \\ \\  \\    /  / |   ____| |   _   \\   |  |
            /  | |  \\ \\  \\  /  /  |  |__    |  |_|   \\  |  |
           |   | |   | \\  \\/  /   |   __|   |   _   /   |__|
            \\   -   /   \\    /    |  |____  |  |  \\  \\   __
             \\_____/     \\__/     |_______| |__|   \\__| |__|

        """


# ###################################################################
#
# Game Loop
#
# ###################################################################
def game_loop(board: Board, tile: Tile) -> bool:
    """Game Flow - Game Loop

    Args:
        board (Board): The board the game is played on
        tile (Tile): The players starting tile

    Returns:
        bool: True if user cleared the board, False if the user died
    """
    game_run = True
    while game_run:
        print(board)

        coordinates = player_move_menu(tile)
        # sudden Game Exit
        if coordinates is None:
            return False
        target = board.get_tile(coordinates)
        # out of bounds
        if target is None:
            print('You run into a wall, it hurt your head a bit but you\'ll survive.')
            continue
        # battle
        if target.monsters:
            isalive = battle(player=tile.player, monsters=target.monsters)
            if not isalive:
                game_over()
                return False
            if target.monsters:  # player fled from battle
                target.explored = True
                continue
        # treasure
        if target.treasure:
            print('[Control Flow] [Game Loop] target.treasure')
            # player pickup treasure
        # exit
        if target.exit:
            print('[Control Flow] [Game Loop] target.exit')
            # exit yes or no?
            # and then return True

        print(f'[Control Flow] [Game Loop] move_player({tile}, {target})')
        tile = move_player(tile, target)


def player_move_menu(tile: Tile) -> Union[Tuple[int, int], None]:
    """[summary]

    Returns:
        tuple: The coordinates the player is trying to move towards
        None: The player decided to stop playing
    """
    choices = [('w', 'Go North'), ('a', 'Go West'), ('s', 'Go South'), ('d', 'Go East')]
    choice = user_choice(choices)
    if choice == 'w':
        coordinates = (tile.x, tile.y + 1)
    elif choice == 'a':
        coordinates = (tile.x - 1, tile.y)
    elif choice == 's':
        coordinates = (tile.x, tile.y - 1)
    elif choice == 'd':
        coordinates = (tile.x + 1, tile.y)
    return coordinates


def move_player(old: Tile, new: Tile) -> None:
    """Move the player object from Tile `old` to Tile `new`

    Args:
        old (Tile): [description]
        new (Tile): [description]
    """
    pass


# ###################################################################
#
# Battle Loop
#
# ###################################################################
def battle(player: Character, monsters: List[Monster]) -> bool:
    """Game Flow - Battle Loop

    Args:
        player (Character): [description]
        monsters (list: [description]

    Returns:
        bool: is the user still alive?
    """
    pass


def flee_battle(player: Character) -> bool:
    flee_chance = player.evasion * 10
    random_roll = random.randint(0, 100)
    if player.__class__.__name__ == "Wizard":
        flee_chance = 80
    if flee_chance > random_roll:
        print('You managed to escape!\n')
        return True
    print('You failed to escape.\n')
    return False


def print_battle_menu(player, monsters):  # need to align hp values

    monster_info = ''
    for monster in monsters:
        monster_info += str(monster) + ' ' + str(monster.health)

        if (monsters.index(monster) != len(monsters)-1):
            monster_info += '\n'

    above = 'Name\tHealth\n- - - - - - - - - -\n' + player.name + ' ' + str(player.health) + '\n' + monster_info + '\n- - - - - - - - - -'

    choices = [
        ('1', 'Attack'),
        ('2', 'Flee')
    ]
    choice = user_choice(choices, above=above)
    return choice


# ###################################################################
#
# Game End
#
# ###################################################################
def game_over():
    print(GAME_OVER)
    time.sleep(2)
