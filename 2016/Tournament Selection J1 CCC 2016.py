num_of_wins=0

for current_game in range(6):
    game_result=input()

    if (game_result=='W'):
        num_of_wins+=1
        
if (num_of_wins>=5):
    group=1
elif ((num_of_wins==3) or (num_of_wins==4)):
    group=2
elif ((num_of_wins==1) or (num_of_wins==2)):
    group=3
else:
    group=-1

print(group)
