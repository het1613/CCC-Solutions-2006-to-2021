P=int(input())
N=int(input())
R=int(input())

total=N
new=N*R
day=0

while total<P:
    total+=new
    new*=R
    day+=1

print(day)
