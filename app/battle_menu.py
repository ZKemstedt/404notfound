import character
import monster
import board
import random


def print_btl_menu(player): # need to add monsters
    name_list = [[]]
    #Temporary storing in list to get the print menu to work
    name_list[0].append('Zombie')
    #a = monster.health
    #b = monster.name
    name_list[0].append(1)
    name_list.append([])
    #Everything above this needs to be changed
    full_str = ''
    monster = 2
    for _ in range(1): # in range monster
        full_str += name_list[_][0] + '\t\t' + str(name_list[_][1]) + '\n'
    full_str = full_str[:-1]    #remove last NewLine
    
    menu_choice = input(f"""
Name\t\tHealth
- - - - - - - - - - - 
{full_str}
{player.name}\t\t{player.health}
- - - - - - - - - - - 
[ 1 ] Attack
[ 2 ] Flee\n""")
    return menu_choice

    
elsa = character.Character('Elsa', 15, 1, 4, 15)
abbe = character.Character('micke', 11, 2, 7, 9)
monster = monster.Monster(2, 3, 3, 4, 0.15)


def dice(x) -> int:
    dice_sum = 0
    for _ in range(1,x+1):
        print('_ ====' , _)
        dice_sum += random.randint(1,6)
        print(dice_sum)
    return dice_sum


tile = board.Tile(0,0)
x = tile.monsters
x.append('scarymonsta')
x.append(1)


def fight(player):
    cmd = print_btl_menu(elsa)
    #Player has entered fight and chosen 1, (fight!)
    if(cmd == '1'):
        
        attack_value = dice(player.power)
        #attack value is the dice_sum, dice thrown for each point of power

    
def fighting(attacker, defender):
    print('axax')
    
    
    


fight(elsa)