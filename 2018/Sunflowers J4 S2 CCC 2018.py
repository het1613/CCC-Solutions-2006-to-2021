def rotate(num,original):
    new=[]

    for column in range(num-1,-1,-1):
        temp=[]
        for row in range(num):
            temp.append(original[row][column])
        new.append(temp)

    return new

num=int(input())

original=[]
row_check=False
column_check=False

for rows in range(num):
    temp_row=input()
    original.append(temp_row.split())

while True:
    for row in range(num):
        if (original[row]!=sorted(original[row])):
            row_check=False
            break
    else:
        row_check=True

    for row in range(num):
        temp_column=[]
        for column in range(num):
            temp_column.append(original[column][row])
            
        if (temp_column!=sorted(temp_column)):
            column_check=False
            break
    else:
        column_check=True

    if ((row_check==True) and (column_check==True)):
        break

    original=rotate(num,original)

print()

for row in range(num):
    print(' '.join(original[row]))

    
    
    
