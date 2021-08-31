#Programmer: Het Patel
#Date Written: 9/17/20
#Version: 1.0
#Purpose: Output array of distances between cities

distances=input('Enter the distances between the cities: ').split()

for current_distance in range(len(distances)):
    distances[current_distance]=int(distances[current_distance])

first_row=[0]

for current_distance in range(4):
    first_row.append(first_row[-1]+distances[current_distance])

for current_city in range(5):
    new_row=[]

    for current_distance in range(5):
        distance=abs(first_row[current_distance]-first_row[current_city])
        new_row.append(str(distance))

    print(' '.join(new_row))
