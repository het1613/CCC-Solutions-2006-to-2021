#Het Patel
#J3 CCC 2021
#17/02/20

outputs=[]

while True:
    current=input()

    if current=='99999': break

    current=list(current)
    digit_sum=int(current[0])+int(current[1])

    if digit_sum%2==1: direction="left"
    elif digit_sum%2==0: direction="right"

    outputs.append(direction+' '+str(''.join(current[2:])))

print('\n'.join(outputs))
