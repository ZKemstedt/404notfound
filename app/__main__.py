# Menus and interactions before the game starts and after the game ends
#
# [ App start ]
#
# Main Menu
#   New Character
#   Load Character
#       Setup Game Loop
#       -> Setup Character
#       -> Setup Board + Place Character
#       Run Game Loop
#       -> [ stuff ]
#       Game Loop End
#   Save Character
#   Exit Game
#
# [ App End ]
from typing import Tuple, Union

from app.board import Board, BOARDSIZE, Tile
from app.character import Character, Wizard, Thief, Knight
from app.helpers import user_choice
from app.save_load_data import load_character, save_character
from app.game import game_loop

TITLE = """
         __________                                                                            __
        |    __     \\   ___    ___  ____      __    ________   ________    _______   ____     |  |
        |   |   \\    \\ |   |  |   ||     \\   |  |  /   _____\\ |   _____| /   __    \\|     \\   |  |
        |   |    |    ||   |  |   ||  |\\  \\  |  | /  /   ___  |  |____  |   /  \\   ||  |\\  \\  |  |
        |   |   /    / |   |  |   ||  | \\  \\ |  ||   |  |_  | |   ____| |  |    |  ||  | \\  \\ |  |
        |    --     /  |   |__|   ||  |  \\  \\|  | \\   \\__/  / |  |_____ |   \\__/   ||  |  \\  \\|  |
         ----------     \\________/ |__|   \\_____|   \\______/  |________| \\________/ |__|   \\_____|
                                 ______    ___    ___  ____      __
                                |   __  \\ |   |  |   ||     \\   |  |
                                |  |  |  ||   |  |   ||  |\\  \\  |  |
                                |   --  / |   |  |   ||  | \\  \\ |  |
                                |  |\\   \\ |   |__|   ||  |  \\  \\|  |
                                |__| \\___\\ \\________/ |  |   \\_____|
                                                      |__|
"""


def main_menu():
    print(TITLE)
    menu_loop = True
    while menu_loop:
        try:
            menu_choice = int(input("""
                                        [ 1 ] Load Character\n
                                        [ 2 ] Save Character\n
                                        [ 3 ] Exit Game

                                        Make a move: """))
            if menu_choice == 3:
                return exit()
            else:
                return menu_choice
        except ValueError:
            print('\n\n\t\t\tYou can only enter an integer!\n\n')


# ###################################################################
#
# Setup Character
#
# ###################################################################

def setup_character(is_new: bool) -> Union[Character, None]:
    print('[Control Flow] [Setup Character] setup_character')
    name = enter_character_name()
    if is_new:
        choice = choose_character_type()
        character = create_character(choice, name)
    else:
        character = load_character(name)
    return character


def create_character(choice: int, name: str) -> Character:
    # print('[Control Flow] [Setup Character] create_character')
    choice_to_class = {
        1: Knight,
        2: Wizard,
        3: Thief
    }
    return choice_to_class[choice](name)


def enter_character_name():
    name = input('Enter the character name: ')
    return name


def choose_character_type():
    correct_answer = [1, 2, 3]
    error = ('You can only enter 1, 2 or 3')
    while True:
        try:
            choice = int(input(
                'Choose character type.\n'
                '(1) Knight, (2) Wizard or (3) Thief.\n'
                ))
        except ValueError:
            print(error)

        if choice in correct_answer:
            return choice
        else:
            print(error)


# ###################################################################
#
# Setup Board
#
# ###################################################################
def setup_board(character: Character) -> Tuple[Board, Tile]:
    """Game Flow - Setup Board"""
    print('[Control Flow] [Main Menu] setup_board')
    # board
    boardsize = select_board_size()
    board = Board(*boardsize)
    # place player
    start_tile = select_start_position(board, character)
    start_tile.place_character(character)
    return board, start_tile


def select_board_size():
    # print('[Control Flow] [Setup Board] select_board_size')
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

    return BOARDSIZE[diffpick]


def select_start_position(board: Board, character: Character) -> Tile:
    """Ask the user in what corner of the board they wish to start and return the corresponding tile object.

    Args:
        board: the board object

    Returns:
        tile: The tile to place the player on
    """
    # print('[Control Flow] [Setup Board] select_start_position')
    # find corners -> get user choice -> convert to coordinates -> get tile -> place character on tile

    north = board.sizey - 1
    south = 0
    east = board.sizex - 1
    west = 0

    above = '\nChoose in which corner of the board to start your adventure.'
    choices = [
            ('1', 'Top left (North West)'),
            ('2', 'Top Right (North East)'),
            ('3', 'Bottom Left (South West)'),
            ('4', 'Bottom Right (South East)')
        ]
    choice = user_choice(choices, above=above)
    if choice == "1":
        coordinates = (north, west)
    elif choice == "2":
        coordinates = (north, east)
    elif choice == "3":
        coordinates = (south, west)
    elif choice == "4":
        coordinates = (south, east)

    tile = board.get_tile(coordinates)
    return tile


# ###################################################################
#
# Run Game Loop
#
# ###################################################################

# TODO


# ###################################################################
#
# Game End / Save Character
#
# ###################################################################

# TODO


if __name__ == "__main__":
    while True:
        choices = [
            ('1', 'New Character'),
            ('2', 'Load Character'),
            ('3', 'Exit Game'),
        ]
        sep = "\n                                        "
        choice = user_choice(choices, above=TITLE, exception='3', separator=sep)

        if choice == '3':
            # print('[Control Flow] [Main Menu] exit')
            break
        if choice == '1':
            is_new = True
        elif choice == '2':
            is_new = False

        # setup character
        character = setup_character(is_new)
        if character is None:
            continue

        # setup board
        board, start_tile = setup_board(character)

        # run game
        is_win = game_loop(board, start_tile)
        if is_win:
            # save character
            save_character(board.get_character())

    print('Thanks for playing :)')
