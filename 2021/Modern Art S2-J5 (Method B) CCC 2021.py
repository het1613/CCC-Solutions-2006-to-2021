#Het Patel
#S2 CCC 2021
#17/02/20

rows=int(input())
columns=int(input())
num=int(input())

orders=[]
R=0
C=0
for i in range(num):
    current=input()
    temp=1
    if current not in orders:
        orders.append(current)
    else:
        orders.remove(current)
        temp*=-1
    if current[0]=="R": R+=temp
    else: C+=temp

total=R*columns+C*rows-2*C*R
print(total)
