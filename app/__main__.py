# Menus and interactions before the game starts and after the game ends
#
# [ App start ]
#
# Main Menu
#   New Character
#   Load Character
#       Setup Game Loop
#       -> Setup Character
#       -> Setup Board
#       -> Place Character
#       Run Game Loop
#       -> [ stuff ]
#       Game Loop End
#   Save Character
#   Exit Game
#
# [ App End ]

from typing import Tuple, List, Optional

BOARDSIZE = {
    '1': (4, 4),
    '2': (5, 5),
    '3': (8, 8)
}

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


def user_choice(
    menu_items: List[Tuple[str, str]],
    *,
    above: Optional[str] = '\n',
    below: Optional[str] = '\n',
    separator: Optional[str] = '\n',
    prompt: Optional[str] = '> ',
    invalid: Optional[str] = None,
    exception: Optional[str] = None,
    error_string: Optional[str] = 'Invalid choice'
) -> str:
    """Prompts the user to choose an option from a menu and return the corresponding key.

    Args:
        menu_items (list): a list of tuples representing the menu items: (key, description)
                    where key is the expected value the user will enter as well as the value to return.
                    And description is the description of said choice

        above (str): optional, string to print above the list of menu options. Defaults to a linebreak
        below (str): optional, string to print below the list of menu options. Defaults to a linebreak
        separator (str): optional, string used to separate the menu options. Defaults to a linebreak
        prompt (str): optional, the string used when prompting the user for input. Defaults to `> `
        invalid (str): optionl, if set; return said value when the user enters an invalid choice.
        exception (str): optional, if set; return said value when the user raises `KeyboardInterrupt`.
        error_string (str): optional, string to print when the user enters an invalid choice.

    Returns:
        choice (str): one of the specified correct choices
        invalid (str): if provided as argument and user enters an invalid choice
        exception (str): if provided as argument and users raises `KeyboardInterrupt`
    """
    choices = []
    text = above
    for key, description in menu_items:
        text += f'[ {key} ]  {description}'
        text += separator
        choices.append(key)
    text += below

    print(text)
    while True:
        try:
            choice = input(prompt)
            if choice in choices:
                return choice
            elif invalid:
                return invalid
            elif error_string:
                print(error_string)

        except KeyboardInterrupt:
            if exception:
                return exception
            elif error_string:
                print(error_string)


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


def choose_start_position():
    choose_position = input("Choose from where you want to start game:\n 1.Top left \n 2.Top right \n 3.Bottom left \n 4.Bottom right")

    if choose_position == "1":
        start_pos = (0, 0)

    elif choose_position == "2":
        start_pos = (0, (sizey -1))

    elif choose_position == "3":
        start_pos = ((sizex -1), 0)

    elif choose_position == "4":
        start_pos = ((sizex -1), (sizey -1))

    # TODO
    else:
        pass

    return start_pos


def choose_board_size():
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


if __name__ == "__main__":

    # This is an alternative Main Menu Example
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
        print('(example) [Control Flow] Main Menu -> exit')
        exit()
    else:
        print('(example) [Control Flow] Main Menu -> \"Setup Board\"')
        # setup the game and run it
