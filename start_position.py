# 'sizex' och 'sizey' defined in Board class

choose_position = input("Choose from where you want to start game:\n 1.Top left \n 2.Top right \n 3.Bottom left \n 4.Bottom right")

if choose_position == "1":
    start_pos = (0, 0)

if choose_position == "2":
    start_pos = (0, (sizey -1))

if choose_position == "3":
    start_pos = ((sizex -1), 0)

if choose_position == "4":
    start_pos = ((sizex -1), (sizey -1))
