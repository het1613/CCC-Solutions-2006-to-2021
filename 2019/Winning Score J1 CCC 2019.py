team_A_points=0
team_B_points=0

for point_value in range(3,0,-1):
    num_of_shots=int(input())
    team_A_points+=(point_value*num_of_shots)

for point_value in range(3,0,-1):
    num_of_shots=int(input())
    team_B_points+=(point_value*num_of_shots)

if (team_A_points>team_B_points):
    winner='A'

elif (team_A_points<team_B_points):
    winner='B'

else:
    winner='T'

print(winner)

    
    
