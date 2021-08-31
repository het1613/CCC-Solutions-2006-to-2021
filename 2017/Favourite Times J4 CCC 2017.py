duration=int(input('Enter the number of minitues the clock was observed: '))

time=[1,2,0,0]
counter=0

for iteration in range(duration):
    time[3]+=1

    if (time[3]>9):
        time[2]+=1
        time[3]=0

    if (time[2]>5):
        time[1]+=1
        time[2]=0

    if (time[0:2]==[1,3]):
        time[0]=0
        time[1]=1

    if (time[1]==10):
        time[0]=1
        time[1]=0
        
    if (time[0]!=0):
        if ((time[3]-time[2])==(time[2]-time[1])==(time[1]-time[0])):
            counter+=1
            print('{0}{1}:{2}{3}'.format(time[0],time[1],time[2],time[3]))
            
    elif ((time[3]-time[2])==(time[2]-time[1])):
        counter+=1
        print('{0}:{1}{2}'.format(time[1],time[2],time[3]))

print('\nThe number of times that the clock displays an arithmetic sequence is {}.'.format(counter))

    
