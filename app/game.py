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


# To be merged into Game Loop Menu / Player Move Loop
def pause_menu():
    choice = input('Do you want to 1: Exit the game or 2: Continue?')
    if (choice == 1):
        pass
    elif (choice == 2):
        pass
    else:
        pass


def moveMenu():
    while True:
        choices = [('w', 'Go North'), ('a', 'Go West'), ('s', 'Go South'), ('d', 'Go East')]
        choice = user_choice(choices)
            if choice == 'w':
                coordinates = (tile.x, tile.y + 1)
            elif choice == 'a':
                coordinates = (tile.x -1, tile.y)
            elif choice == 's':
                coordinates = (tile.x, tile.y - 1)
            elif choice == 'd':
                coordinates = (tile.x + 1, tile.y)
    return coordinates