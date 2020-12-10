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
from typing import List, Union

from app.board import Board, Tile
from app.monster import Monster
from app.character import Character

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
        target = player_move_menu()  # target: Tile or None

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


def player_move_menu() -> Union[Tile, None]:
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

    new.player = old.player
    old.player = None
    old.explored = True


# To be merged into Game Loop Menu / Player Move Loop
def pause_menu():
    choice = input('Do you want to 1: Exit the game or 2: Continue?')
    if (choice == 1):
        pass
    elif (choice == 2):
        pass
    else:
        pass
