rounds=int(input('Enter number of rounds: '))

antonia_points=100
david_points=100

for current_round in range(rounds):
    rolls=input('Enter round: ').split()
    rolls=[int(element) for element in rolls]

    if (rolls[0]>rolls[1]):
        david_points-=rolls[0]
        
    elif (rolls[0]<rolls[1]):
        antonia_points-=rolls[1]

print('Antonia Points: {}'.format(antonia_points))
print('David Points: {}'.format(david_points))     
