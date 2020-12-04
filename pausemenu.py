

def pausMenu():
    a = input('Do you want to 1: Exit the game or 2: Continue?')
    if (a == 1):
        break
    elif (a == 2):
        continue    
    else:
        print('Try again')
        pass

pausMenu()