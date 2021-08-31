start=int(input('Enter start number: '))
end=int(input('Enter end number: '))

counter=0

for number in range(start,end+1):
    square=round(number**(1/2))
    cube=round(number**(1/3))

    if ((square**2==number) and (cube**3==number) and (square%1==0) and (cube%1==0)):
        print(number)
        counter+=1

print('There are {} cool numbers.'.format(counter))
