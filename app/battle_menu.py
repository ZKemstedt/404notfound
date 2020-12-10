import character
import monster


def battle_menu(player, monster):
    menu_choice = print_btl_menu(player, monster)
    if menu_choice == '1':
        print('attack')
        #Choose which monster to attack
    elif menu_choice == '2':
        print('flee')
        #Attempt flee
    elif menu_choice == '3':
        print('exit game')
    else:
        print('Invalid command, try again from the menu')
#How do we treat two monsters on same tile?


def print_btl_menu(player, monster):
    name_list = [[]]
    #Temporary storing in list to get the print menu to work
    name_list[0].append('Zombie')
    a = monster.health
    #b = monster.name
    name_list[0].append(1)
    name_list.append([])
    name_list[1].append('Troll')
    name_list[1].append(2) 
    #Everything above this needs to be changed
    full_str = ''
    monster = 2
    for _ in range(monster):
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

    
battle_menu(character.Character('Elsa', 15, 1, 1, 1), monster.Monster(2, 3, 3, 4, 0.15))
ab = monster.Monster(2, 3, 3, 4, 0.15)

