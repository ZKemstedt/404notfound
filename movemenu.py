def moveMenu():
    move = input('Which way do you want to move?\nW: Up, A: Left, S: Down, D: Right\n')
    while True:
     for x in range(MAPWIDTH):
         for y in range(MAPHEIGHT):
             if tile[x][y] == wall:
                 print('Wall, try another way!')
                 pass

                if move.lower() == 'w':
                    tile[y+1]
                elif move.lower() == 'a':
                    tile[x-1]
                elif move.lower() == 's':
                    tile[y-1]
                elif move.lower() == 'd':
                    tile[x+1]
                else:
                    print('Not a valid choice, try again')
                    return