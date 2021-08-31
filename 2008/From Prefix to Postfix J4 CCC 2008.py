#Programmer: Het Patel
#Date Written: 9/21/20
#Version: 1.0
#Purpose: To convert prefix prefix to postfix prefixs

while True:

    prefix=(input('\nEnter a prefix expression: ').split())[::-1]

    if prefix==['0']:
        break

    postfix=[]
    
    for current in prefix:
        
        if ((current=='+') or (current=='-')):
            num1=postfix[-1]
            num2=postfix[-2]
            postfix=postfix[:-2]
            postfix.append(num1+num2+current+' ')

        else:
            postfix.append(current+' ')
            
    print(' '.join(postfix))
