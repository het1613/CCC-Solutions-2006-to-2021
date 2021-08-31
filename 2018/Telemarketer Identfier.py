#Programmer: Het Patel
#Date Written: 11/01/19
#Version: 1.0
#Prupose: To identify a telemarketer phone number from given conditions

num=str(int(input('Enter the last 4 digits of the phone number: ')))

if ((num[0]=='8') or (num[0]=='9')) and ((num[3]=='8') or (num[3]=='9')) and (num[1]==num[2]):
    print('IGNORE')

else:
    print('ANSWER')
    
    
