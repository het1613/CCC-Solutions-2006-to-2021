last_4=[]

for digit in range(4):
    last_4.append(int(input()))

if ((last_4[0]==8) or (last_4[0]==9)):
    if ((last_4[3]==8) or (last_4[3]==9)):
        if (last_4[1]==last_4[2]):
            print('IGNORE')

else:
    print('ANSWER')
