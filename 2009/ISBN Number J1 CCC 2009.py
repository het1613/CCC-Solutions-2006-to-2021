#Programmer: Het Patel
#Date Written: 9/20/20
#Version: 1.0

ISBN_num=eval(input('Enter a 13-digit number: '))

total_sum=0

for pos in range(13):
    if (pos%2==0):
        total_sum+=int(str(ISBN_num)[pos])
    else:
        total_sum+=int(str(ISBN_num)[pos])*3

print('\nThe 1-3-sum is',total_sum)
