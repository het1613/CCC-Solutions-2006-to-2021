#Het Patel
#S3 CCC 2021
#17/02/20

def time_finder(pos):
    global info

    total_time=0
    for friend in info:
        starting=friend[0]
        speed=friend[1]
        hearing=friend[2]

        move=0
        if abs(pos-starting)>hearing:
            move=abs(pos-starting)-hearing
        total_time+=speed*move
    return total_time


num_of_friends=int(input())
info=[[int(j) for j in input().split()] for i in range(num_of_friends)]

min=9999999999999
max=-1
for friend in info:
    if friend[0]-friend[2]<min:
        min=friend[0]-friend[2]
    if friend[0]+friend[2]>max:
        max=friend[0]+friend[2]
if min<0:
    min=0

min_time=999999999999
for distance in range(min, max+1):
    current_time=time_finder(distance)
    if current_time<min_time:
        min_time=current_time

print(min_time)
