#Programmer: Het Patel
#Date Written: 12/07/19
#Version: 1.0
#Purpose: To determine the least number of moves needed to move a knight from start to end position.

global end
global possible

def next_move(current,j,n):
    x=current[0]+j[0]
    y=current[1]+j[1]
    current=[x,y]

    if current==end:
        possible.append(n)

    return current

start=input()
end=input()

start=start.split(' ')
end=end.split(' ')

current=[int(i) for i in start]
end=[int(i) for i in end]

moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

possible=[]

for i in moves:
    current=next_move(current,i,1)
        
    for j in moves:
        current=next_move(current,j,2)

        for k in moves:
            current=next_move(current,k,3)

print(min(possible))
