#Programmer: Het Patel
#Date Written: 9/17/20
#Version: 1.0
#Purpose: To output the sum of the number with all shifted n number of times

num=int(input('Enter a number: '))
shift_num=int(input('Enter the number of times to shift: '))

total_sum=num

for current_shift in range(1,shift_num+1):
    total_sum+=num*(10**current_shift)

print('The shifty sum of {}, {} times is {}.'.format(num,shift_num,total_sum))
    
