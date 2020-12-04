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

def pause_menu():
    choice = input('Do you want to 1: Exit the game or 2: Continue?')
    if (choice == 1):
        break
    elif (choice == 2):
        continue
    else:
        print('Try again')
        pass
