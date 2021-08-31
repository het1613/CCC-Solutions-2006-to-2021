num_of_lines=int(input())

min_x=100
max_x=0

min_y=100
max_y=0

for line in range(num_of_lines):
    x=input()
    coordinate=x.split(',')

    for i in range(len(coordinate)):
        coordinate[i]=int(coordinate[i])

    if coordinate[0]<min_x:
        min_x=coordinate[0]
        
    if coordinate[0]>max_x:
        max_x=coordinate[0]

    if coordinate[1]<min_y:
        min_y=coordinate[1]
        
    if coordinate[1]>max_y:
        max_y=coordinate[1]

bottom_left=str(min_x-1)+','+str(min_y-1)
top_right=str(max_x+1)+','+str(max_y+1)

print(bottom_left)
print(top_right)


    
    
