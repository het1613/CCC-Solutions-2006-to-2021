max_weight=int(input())

num_of_cars=int(input())

car_weights=[int(input()) for current_car in range(num_of_cars)]

max_cars=0

current_weight=0

pos=0

while ((pos<3) and (pos<num_of_cars-1)):

    current_weight+=car_weights[pos]

    if (current_weight>max_weight):
        break
    
    pos+=1
    
else:
    
    for pos in range(num_of_cars-2):

        current_weight=sum(car_weights[pos:pos+4])

        if (current_weight>max_weight):
            pos+=3
            break

print(pos)
    
