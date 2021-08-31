#Programmer: Het Patel
#Date: 10/23/2019
#Version: 1.0
#Purpose: To output the next closest year with all distinctive digits

year=str(int(input('Enter a year: '))+1)

while True:
    for digit in year:
        if (year.count(digit)>1):
            year=str(int(year)+1)
            break
    else:
        break

print('The next year with all distinctive digits is:',year)
