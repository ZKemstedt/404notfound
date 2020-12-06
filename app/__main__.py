
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
     ___________                                                                           __
    |    _ _    \   ___    ___  ___       __    ________   ________  ___    ___  ___      |  |
    |   |   \    \ |   |  |   ||    \    |  |  /   _____\ |   _____||   |  |   ||    \    |  |
    |   |    |    ||   |  |   ||     \   |  | /  /   ____ |  |____  |   |  |   ||     \   |  |
    |   |   /    / |   |  |   ||  |\   \ |  ||   |  |_  | |   ____| |   |  |   ||  |\   \ |  |
    |   - -    /   |   |__|   ||  |  \  \|  | \   \__/  / |  |_____ |   |__|   ||  |  \  \|  |
     ----------     \________/ |__|   \_____|   \______/  |________| \________/ |__|   \_____|
                               ______    ___    ___  ___       __ 
                              |   _   \ |   |  |   ||    \    |  |
                              |  |  |  ||   |  |   ||     \   |  |
                              |   --  / |   |  |   ||  |\   \ |  |
                              |  |\   \ |   |__|   ||  |  \  \|  |
                              |__| \___\ \________/ |  |   \_____| 
                                                    |__|
        """)
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
        print('Ops, you can only enter an integer!')
