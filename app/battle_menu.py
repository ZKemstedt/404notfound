import random
# from app import character
# from app import monster
# from app import board
# from app.helpers import user_choice
import character
import monster
import board
from helpers import user_choice


def print_battle_menu(player, monsters):  # need to add monsters
    # name_list = [[]]
    # name_list[0].append('Zombie')
    # name_list[0].append(1)
    # name_list.append([])
    # full_str = ''
    # for _ in range(1): # in range monster
    #    full_str += name_list[_][0] + '\t\t' + str(name_list[_][1]) + '\n'
    # full_str = full_str[:-1]    #remove last NewLine
    choices = [
        ('1', 'Attack'),
        ('2', 'Flee')
    ]
    choice = user_choice(choices)
    return choice

#     menu_choice = input(f"""
# Name\t\tHealth
# - - - - - - - - - - -
# {full_str}
# {player.name}\t\t{player.health}
# - - - - - - - - - - -
# [ 1 ] Attack
# [ 2 ] Flee\n""")
#     return menu_choice


def dice(x) -> int:
    dice_sum = 0
    for _ in range(1,x+1):
        print('_ ====' , _)
        dice_sum += random.randint(1,6)
        print(dice_sum)
    return dice_sum


# tile = board.Tile(0,0)
# x = tile.monsters
# x.append('scarymonsta')
# x.append(1)


def fight(player):
    cmd = print_btl_menu(elsa)
    # Player has entered fight and chosen 1, (fight!)
    if(cmd == '1'):

        attack_value = dice(player.power)
        # attack value is the dice_sum, dice thrown for each point of power


def fighting(attacker, defender):
    print('axax')


# fight(elsa)

if __name__ == "__main__":
    elsa = character.Character('Elsa', 15, 1, 4, 15)
    abbe = character.Character('Micke', 11, 2, 7, 9)
    monster = monster.Monster(2, 3, 3, 4, 0.15)
    print_battle_menu(elsa, [monster])
