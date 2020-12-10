import random
# from app import character
# from app import monster
# from app import board
# from app.helpers import user_choice
import character
import monster
import board
from helpers import user_choice


def print_battle_menu(player, monsters):  # need to align hp values
    
    monster_info = ''
    for _ in monsters:
        monster_info += str(_) + ' ' + str(_.health)

        if (monsters.index(_) != len(monsters)-1):
            monster_info += '\n'

    battle_info = 'Name\tHealth\n- - - - - - - - - -\n' + player.name + ' ' + str(player.health) + '\n' + monster_info + '\n- - - - - - - - - -'
    
    choices = [
        ('1', 'Attack'),
        ('2', 'Flee')
    ]
    choice = user_choice(choices, above=battle_info)
    return choice


def dice(x) -> int:
    dice_sum = 0
    for _ in range(1, x+1):
        print('_ ====', _)
        dice_sum += random.randint(1, 6)
        print(dice_sum)
    return dice_sum


def fight(player):
    cmd = print_battle_menu(elsa)
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
    monster = monster.Troll()
    #monster.Monster(3, 4, 4, 6, 0.1, 'Orc')
    #monster = monster.Monster(1, 3, 2, 7, 0.2, 'Giant Spider')
    print_battle_menu(elsa, [monster])


    