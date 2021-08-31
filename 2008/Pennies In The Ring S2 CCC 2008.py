output=[]

while True:
    radius=int(input("Enter the circle's radius: "))

    if (radius==0):
        break

    total_coins=0

    for pos in range(1,radius+1):
        total_coins+=int((((radius**2)-(pos**2))**(1/2))+1)
    
    total_coins=total_coins*4+1

    output.append(str(total_coins))

print('\n'.join(output))
