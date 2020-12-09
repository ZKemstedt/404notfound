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
from app.board import Board, BOARDSIZE
from app.character import Character
from app.helpers import user_choice
from app.save_load_data import load_character, save_character

TITLE = """
        __________                                                                            __
    |    __     \\   ___    ___  ____      __    ________   ________  ___    ___  ____     |  |
    |   |   \\    \\ |   |  |   ||     \\   |  |  /   _____\\ |   _____||   |  |   ||     \\   |  |
    |   |    |    ||   |  |   ||  |\\  \\  |  | /  /   ___  |  |____  |   |  |   ||  |\\  \\  |  |
    |   |   /    / |   |  |   ||  | \\  \\ |  ||   |  |_  | |   ____| |   |  |   ||  | \\  \\ |  |
    |    --     /  |   |__|   ||  |  \\  \\|  | \\   \\__/  / |  |_____ |   |__|   ||  |  \\  \\|  |
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

# Placeholder
def load_character():
    print('(example) [Control Flow] Main Menu -> load_character')
    return 'example'


# Placeholder
def create_character():
    print('(example) [Control Flow] Main Menu -> create_character')
    return 'example'


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
def setup_board(character: Character):
    """Game Flow - Setup Board"""
    print('[Control Flow] [Main Menu] setup_board')
    board = select_board_size()
    select_start_position(board, character)
    return board


def select_board_size():
    print('[Control Flow] [Setup Board] select_board_size')
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


def select_start_position(board: Board, character: Character) -> None:
    """Ask the user in what corner of the board they wish to start and return the corresponding tile object.

    Args:
        board: the board object

    Returns:
        tile: The tile to place the player on
    """
    print('[Control Flow] [Setup Board] select_start_position')
    # find corners -> get user choice -> convert to coordinates -> get tile -> place character on tile

    north = board.sizey - 1
    south = 0
    east = board.sizex - 1
    west = 0

    choices = [
            ('1', 'Top left (North West)'),
            ('2', 'Top Right (North East)'),
            ('3', 'Bottom Left (South West)'),
            ('4', 'Bottom Right (South East)')
        ]
    choice = user_choice(choices)
    if choice == "1":
        coordinates = (north, west)
    elif choice == "2":
        coordinates = (north, east)
    elif choice == "3":
        coordinates = (south, west)
    elif choice == "4":
        coordinates = (south, east)

    tile = board.get_tile(coordinates)
    tile.place_character(character)


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

    choices = [
        ('1', 'New Character'),
        ('2', 'Load Character'),
        ('3', 'Exit Game'),
    ]
    choice = user_choice(choices, above=TITLE, exception='3')

    if choice == '1':
        character = create_character()
    elif choice == '2':
        character = load_character()

    if choice == '3':
        print('(testing) [Control Flow] Main Menu -> exit')
        exit()
    else:
        board = setup_board(character)
        # setup the game and run it
