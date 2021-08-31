A=0
B=0

while True:
    command=input()

    if command=='7':
        break
    
    command=command.split(' ')

    if command[0]=='1':
        if command[1]=='A':
            A=int(command[2])
        elif command[1]=='B':
            B=int(command[2])

    if command[0]=='2':
        if command[1]=='A':
            print(A)
        elif command[1]=='B':
            print(B)
        
    if command[0]=='3':
        if command[1]=='A' and command[2]=='A':
            A=A+A
        elif command[1]=='B' and command[2]=='B':
            B=B+B
        elif command[1]=='A' and command[2]=='B':
            A=A+B
        elif command[1]=='B' and command[2]=='A':
            B=A+B
    
    if command[0]=='4':
        if command[1]=='A' and command[2]=='A':
            A=A*A
        elif command[1]=='B' and command[2]=='B':
            B=B*B
        elif command[1]=='A' and command[2]=='B':
            A=A*B
        elif command[1]=='B' and command[2]=='A':
            B=A*B

    if command[0]=='5':
        if command[1]=='A' and command[2]=='A':
            A=A-A
        elif command[1]=='B' and command[2]=='B':
            B=B-B
        elif command[1]=='A' and command[2]=='B':
            A=A-B
        elif command[1]=='B' and command[2]=='A':
            B=A-B

    if command[0]=='6':
        if command[1]=='A' and command[2]=='A':
            A=A//A
        elif command[1]=='B' and command[2]=='B':
            B=B//B
        elif command[1]=='A' and command[2]=='B':
            A=A//B
        elif command[1]=='B' and command[2]=='A':
            B=A//B
        
