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
from typing import List, Union, Tuple

from app.board import Board, Tile
from app.monster import Monster
from app.character import Character
from helpers import user_choice

import time


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
        coordinates = player_move_menu()  # target: Tile or None
        target = board.get_tile(coordinates)

        if target is None:  # Sudden Game Exit
            return False  # Do not save

        if target.monsters:
            isalive = battle(player=tile.player, monsters=target.monsters)
            if not isalive:
                game_over()
                return False

        if target.treasure:
            pass  # player pickup treasure

        if target.exit:
            # exit yes or no?
            # and then return True
            return True

        move_player(tile, target)


def game_over():
    print("""
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

        """)
    time.sleep(2)


def battle(player: Character, monsters: List[Monster]) -> bool:
    """Game Flow - Battle Loop

    Args:
        player (Character): [description]
        monsters (list: [description]

    Returns:
        bool: is the user still alive?
    """
    # if dead --> game_over()
    pass


def print_battle_menu(player, monsters):  # need to align hp values
    
    monster_info = ''
    for _ in monsters:
        monster_info += str(_) + ' ' + str(_.health)

        if (monsters.index(_) != len(monsters)-1):
            monster_info += '\n'

    a = 'Name\tHealth\n- - - - - - - - - -\n' + player.name + ' ' + str(player.health) + '\n' + monster_info + '\n- - - - - - - - - -'

    choices = [
        ('1', 'Attack'),
        ('2', 'Flee')
    ]
    choice = user_choice(choices, above=a)
    return choice


def player_move_menu() -> Union[Tuple[int, int], None]:
    """[summary]

    Returns:
        Tile: The tile the player is trying to move towards
        None: The player decided to stop playing
    """
    pass


def move_player(old: Tile, new: Tile) -> None:
    """Move the player object from Tile `old` to Tile `new`

    Args:
        old (Tile): [description]
        new (Tile): [description]
    """
    pass


# To be merged into Game Loop Menu / Player Move Loop
def pause_menu():
    choice = input('Do you want to 1: Exit the game or 2: Continue?')
    if (choice == 1):
        pass
    elif (choice == 2):
        pass
    else:
        pass


def moveMenu():
    while True:
        choices = [('w', 'Go North'), ('a', 'Go West'), ('s', 'Go South'), ('d', 'Go East')]
        choice = user_choice(choices)
            if choice == 'w':
                coordinates = (tile.x, tile.y + 1)
            elif choice == 'a':
                coordinates = (tile.x -1, tile.y)
            elif choice == 's':
                coordinates = (tile.x, tile.y - 1)
            elif choice == 'd':
                coordinates = (tile.x + 1, tile.y)
    return coordinates