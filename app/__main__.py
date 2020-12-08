
# Launcher
#
# Menus and interactions before the game starts and after the game ends
#
# Main Menu
# Load character
# Save character
#

# Dungeon Run

def main_menu():
    print("""
         __________                                                                            __
        |    __     \\   ___    ___  ____      __    ________   ________    _______   ____     |  |
        |   |   \\    \\ |   |  |   ||     \\   |  |  /   _____\\ |   _____| /   __    \\|     \\   |  |
        |   |    |    ||   |  |   ||  |\\  \\  |  | /  /   ___  |  |____  |   /  \\   ||  |\\  \\  |  |
        |   |   /    / |   |  |   ||  | \\  \\ |  ||   |  |_  | |   ____| |  |    |  ||  | \\  \\ |  |
        |    --     /  |   |__|   ||  |  \\  \\|  | \\   \\__/  / |  |_____ |   \\__/   ||  |  \\  \\|  |
         ----------     \\________/ |__|   \\_____|   \\______/  |________| \\________/ |__|   \\_____|
                                 ______    ___    ___  ____      __
                                |   __  \\ |   |  |   ||     \\   |  |
                                |  |  |  ||   |  |   ||  |\\  \\  |  |
                                |   --  / |   |  |   ||  | \\  \\ |  |
                                |  |\\   \\ |   |__|   ||  |  \\  \\|  |
                                |__| \\___\\ \\________/ |  |   \\_____|
                                                      |__|
            """)
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
