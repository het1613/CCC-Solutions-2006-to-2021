dice_1=int(input('Enter m: '))
dice_2=int(input('Enter n: '))

counter=0

for face_1 in range(1,dice_1+1):
    
    for face_2 in range(dice_2,0,-1):
        
        if (face_1+face_2==10):
            counter+=1

if (counter==0):
    status='\nThere is no way to get the sum 10.'

elif (counter==1):
    status='\nThere is 1 way to get the sum 10.'

else:
    status='\nThere are {} ways to get the sum 10.'.format(counter)

print(status)
        
            
