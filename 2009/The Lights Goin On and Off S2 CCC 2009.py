def PushButton(row_1,row_2):
    new=[]

    for pos in range(len(row_1)):
        if (row_1[pos]==row_2[pos]):
            new.append(0)
        else:
            new.append(1)

    return new    

num_of_rows=int(input())

num_of_col=int(input())

lights=[]
above=['' for i in range(256)]
below=['' for i in range(256)]

for row in range(num_of_rows):
    current=[int(i) for i in input().split()]
    lights.append(current)

above[0]=lights[0]

above_size=1
below_size=1

for pos in range(1,num_of_rows):
    below[0]=lights[pos]
    below_size=1

    for pos2 in range(above_size):
        new_row=PushButton(above[pos2],below[0])

        pos3=0

        while(pos3<below_size) and (below[pos3]!=new_row):
            pos3+=1

        if (pos3>=below_size):
            below[below_size]=new_row
            below_size+=1

    for pos4 in range(below_size):
        above[pos4]=below[pos4]
        
    above_size=below_size

print(below_size)

