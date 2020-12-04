# Game loop
#
#   Setup
#       -> Character
#       -> Board
#       -> Place Character
#
#   Run (Loop)
#       -> Display Board
#       -> Move Character
#       -> Pause Game
#
#
#   Exit
#   


def enter_character_name():
    name = input('Enter the characters name: ')


def choose_start_position()
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


def pause_menu():
    choice = input('Do you want to 1: Exit the game or 2: Continue?')
    if (choice == 1):
        break
    elif (choice == 2):
        continue
    else:
        print('Try again')
        pass
