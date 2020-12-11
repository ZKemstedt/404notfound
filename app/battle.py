import monster
import character
import random
from helpers import user_choice
from character import Thief


def print_battle_menu(player, monsters) -> str:

    monster_info = ''
    for monsterrr in monsters:
        monster_info += monsterrr.name + ' ' + str(monsterrr.health)

        if (monsters.index(monsterrr) != len(monsters)-1):
            monster_info += '\n'

    above = 'Name\tHealth\n- - - - - - - - - -\n' + player.name + ' ' + str(player.health) + '\n' + monster_info + '\n- - - - - - - - - -'

    choices = [
        ('1', 'Attack'),
        ('2', 'Flee')
    ]
    choice = user_choice(choices, above=above)
    return choice


def dice(n) -> int:
    dice_sum = 0
    for x in range(n):
        b = random.randint(1, 6)

        dice_sum += b
    return dice_sum


def battle_attack(attacker, defender) -> bool:
    print(f'{attacker.name} attacking!\n')

    if(dice(attacker.power) > dice(defender.evasion)):
        print(f'{defender.name} was sucessfully hit!\n')

        if issubclass(attacker.__class__, Thief) and not random.randint(0, 3):
            print('CRITICAL HIT! Dealt 2 damage')
            defender.health -= 2
        else:
            defender.health -= 1
            print('Dealth 1 damage')

        if(defender.health == 0):
            print(f'{defender.name} has been slain\n')
            return False
    else:
        print('Roll was unsucessfull\nAttack missed!\n')
    return True

# attacker.__class__.__name__
# issubclass(attacker, Thief)


if __name__ == "__main__":
    me = character.Thief('axax')
    monsta = monster.Troll()
    monstaZ = monster.Skeleton()
    while(me.health > 0 and monsta.health > 0):
        x = print_battle_menu(me, [monsta])
        if(x == '1'):
            if (battle_attack(me, monsta)):
                battle_attack(monsta, me)
            else:
                print('donezo')

