humidity=int(input('Enter humidity factor: '))
max_wait=int(input('Enter maximum hours Margaret is willing to wait: '))

for hour in range(1,max_wait+1):
    if ((-6*(hour**4))+(humidity*(hour**3))+(2*(hour**2))+hour)<=0:
        print('The balloon first touches the ground at hour:',hour)
        break
else:
    print('The balloon does not touch the ground in the given time.')
