from math import ceil

num=int(input('Enter a number: '))

count=0

for hand_1 in range(5,ceil(num/2)-1,-1):
    for hand_2 in range(ceil(num/2)+1):
        if (hand_1+hand_2==num):
            count+=1
            
print(count)
