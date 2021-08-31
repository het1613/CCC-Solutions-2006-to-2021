playlist=['A','B','C','D','E']

while True:
    button=int(input('\nButton Number: '))
    
    num=int(input('Number of presses: '))
    
    if (button==4):
        print()
        print(' '.join(playlist))
        break
    
    elif (button==1):
        for iteration in range(num):
            playlist=playlist[1:0]+playlist[:1]

    elif (button==2):
        for iteration in range(num):
            playlist=playlist[4:]+playlist[:4]

    elif (button==3):
        for iteration in range(num):
            playlist=playlist[1:2]+playlist[:1]+playlist[2:]
    
