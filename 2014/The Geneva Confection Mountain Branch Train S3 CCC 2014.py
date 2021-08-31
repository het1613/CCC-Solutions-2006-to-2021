num_of_tests=int(input('Enter number of tests: '))

output=[]

for test in range(num_of_tests):

    num_of_cars=int(input('Enter number of cars: '))

    mountain=[int(input('Enter car number: ')) for car in range(num_of_cars)]

    branch=[]
    
    next_car=1

    status='Y'

    while (next_car<=num_of_cars):
        if ((len(mountain)>0) and (next_car==mountain[-1])):
            mountain.pop(-1)
            next_car+=1

        elif ((len(branch)>0) and (next_car==branch[-1])):
            branch.pop(-1)
            next_car+=1

        elif (len(mountain)>0):
            branch.append(mountain[-1])
            mountain.pop(-1)

        else:
            status='N'
            break

    output.append(status)

print('\n'.join(output))


        
