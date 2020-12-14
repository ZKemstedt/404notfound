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

try:
    from app.board import Board, Tile
    from app.monster import Monster
    from app.character import Character, Thief, Knight
    from app.helpers import user_choice, dice
except ModuleNotFoundError:
    from board import Board, Tile
    from monster import Monster
    from character import Character, Thief, Knight
    from helpers import user_choice, dice


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

BATTLE_STARTED = """
                 ____    _  _____ _____ _     _____
                | __ )  / \\|_   _|_   _| |   | ____|
                |  _ \\ / _ \\ | |   | | | |   |  _|
                | |_) / ___ \\| |   | | | |___| |___
              __|____/_/  _\\_\\_|___|_|_|_____|_____|   _
            / ___|_   _|/ \\  |  _ \\_   _| ____|  _ \\  | |
            \\___ \\ | | / _ \\ | |_) || | |  _| | | | | | |
             ___) || |/ ___ \\|  _ < | | | |___| |_| | |_|
            |____/ |_/_/   \\_\\_| \\_\\|_| |_____|____/  (_)

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
            print(f'[Control Flow] [Game Loop] encountered monsters: {target.monsters}')

            isalive = battle(player=tile.player, monsters=target.monsters)
            if not isalive:
                game_over()
                return False
            if target.monsters:  # player fled from battle
                target.explored = True
                continue

        # treasure
        if target.treasures:
            print(f'[Control Flow] [Game Loop] encountered treasures: {target.treasures}')
            sum_treasure(tile, target)

        # exit
        if target.exit:
            print('[Control Flow] [Game Loop] encountered exit')
            if target.exit_tile():
                return tile.player

        print(f'[Control Flow] [Game Loop] move_player(({tile.x}, {tile.y}), ({target.x}, {target.y}))')
        tile = move_player(tile, target)


def player_move_menu(tile: Tile) -> Union[Tuple[int, int], None]:
    """[summary]

    Returns:
        tuple: The coordinates the player is trying to move towards
        None: The player decided to stop playing
    """
    choices = [
        ('w', 'Go North'),
        ('a', 'Go West'),
        ('s', 'Go South'),
        ('d', 'Go East'),
    ]
    choice = user_choice(choices, exception='0')
    if choice == 'w':
        coordinates = (tile.x, tile.y + 1)
    elif choice == 'a':
        coordinates = (tile.x - 1, tile.y)
    elif choice == 's':
        coordinates = (tile.x, tile.y - 1)
    elif choice == 'd':
        coordinates = (tile.x + 1, tile.y)
    elif choice == '0':
        return None
    return coordinates


def move_player(old: Tile, new: Tile) -> None:
    """Move the player object from Tile `old` to Tile `new`

    Args:
        old (Tile): [description]
        new (Tile): [description]
    """
    new.player = old.player
    old.player = None
    old.explored = True
    return new


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

    # print(BATTLE_STARTED)
    # time.sleep(2)
    # roll dice on who starts the batttle
    # roll_dice_player = dice(monsters[Monster].initiative)
    # roll_dice_monster = dice(player.initiative)
    # print('\n\nTime to roll the dice on who starts the battle!')
    # time.sleep(1)
    # print(f'\n{player}: {roll_dice_player}')
    # time.sleep(1)
    # print(f'{monsters[Monster]}: {roll_dice_monster}')

    # print(BATTLE_STARTED)
    # time.sleep(2)
    # fighters = {}
    # # roll dice on who starts the batttle
    # roll_dice_player = dice(player.initiative)
    # fighters.update({player: roll_dice_player})
    # for x in range(len(monsters)):
    #     monster = monsters[x]
    #     roll_dice_monster = dice(monster.initiative)
    #     fighters.update({monster: roll_dice_monster})

    # print(fighters)

    # fighter_queue = sorted(fighters.items(), key=lambda x: x[1], reverse=True)

    # print(fighter_queue)

    # print('\n\nTime to roll the dice on who starts the battle!')
    # time.sleep(1)
    # print(f'\n{player}: {roll_dice_player}')
    # time.sleep(1)
    # print(f'{monster}: {roll_dice_monster}')

    # # - - - - - check vem som börjar - - - - -
    # if roll_dice_monster > roll_dice_player:
    #     print(f'Oops, {monster} starts the battle!')
    #     # monster attack, player defend
    #     battle_attack(monster, player)
    # else:
    #     battle_loop = True
    #     while battle_loop:
    #         if battle(player) is None:
    #             game_over()  # eller --> /return False ?
    #         choice = print_battle_menu(player, monsters)
    #         if choice == '1':
    #             # player attack, monster defend
    #             battle_attack(player, monster)
    #         elif choice == '2':
    #             # if choice 2 -> Flee
    #             flee_battle(player)

    # testing // Zeph
    print(BATTLE_STARTED)
    time.sleep(2)
    fighters = sorted(monsters + [player], key=lambda x: dice(x.initiative))
    knight = isinstance(player, Knight)
    while True:
        for fighter in fighters:  # ensures the order of attackers
            if fighter is player:
                choice = print_battle_menu(player, monsters)
                if choice == '1':  # player attack
                    choices = [(f'{i+1}', str(monster)) for i, monster in enumerate(monsters)]
                    # longer version:
                    # choices = []
                    # c = 1
                    # for monster in monsters:
                    #     choice = (str(c), str(monster))  # resussing old variable names is not a problem
                    #     choices.append(choice)
                    choice = user_choice(choices, above='\nWhich monster to attack?')
                    monster = monsters[int(choice)-1]
                    if not battle_attack(player, monster):  # ?: monster died
                        fighters.remove(monster)  # remove from fighters
                        monsters.remove(monster)  # remove from tile.monsters
                        if len(fighters) == 1:  # ?: all monsters dead
                            return True
                else:
                    if flee_battle(player):
                        for monster in monsters:
                            monster.reset()
                        return True
            else:  # monster
                if knight:
                    print(f'Knight blocked the hostile {str(fighter).lower()}s attack!')
                    knight = False
                    continue
                if not battle_attack(fighter, player):  # ?: player died
                    return False


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
    for monsterrr in monsters:
        monster_info += f'{str(monsterrr)} {str(monsterrr.health)}'

        if (monsters.index(monsterrr) != len(monsters)-1):
            monster_info += '\n'

    above = ('Name\tHealth\n'
             '- - - - - - - - - -\n'
             f'{player.name} {str(player.health)}\n'
             f'{monster_info}\n- - - - - - - - - -')

    choices = [
        ('1', 'Attack'),
        ('2', 'Flee')
    ]
    choice = user_choice(choices, above=above)
    return choice


def battle_attack(attacker, defender) -> bool:
    print(f'\n{attacker.name} attacking!')

    if(dice(attacker.power) > dice(defender.evasion)):
        print(f'~ {defender.name} was sucessfully hit!')

        if issubclass(attacker.__class__, Thief) and not random.randint(0, 3):
            print('~ CRITICAL HIT! Dealt 2 damage')
            defender.health -= 2
        else:
            defender.health -= 1
            print('~ Dealt 1 damage')

        if(defender.health == 0):
            print(f'~ {defender.name} has been slain\n')
            return False
    else:
        print('~ Attack missed!')
    print('')
    return True


# ###################################################################
#
# Treasure
#
# ###################################################################
def sum_treasure(tile, target):
    for treasure in target.treasures:
        # print(f'[Control Flow] [sum_treasure] adding treasure {treasure}')
        tile.player.treasures += treasure.value
    target.treasures = []


# ###################################################################
#
# Game End
#
# ###################################################################
def game_over():
    print(GAME_OVER)
    time.sleep(2)
