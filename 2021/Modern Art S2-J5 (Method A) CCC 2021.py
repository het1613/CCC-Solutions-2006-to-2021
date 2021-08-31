#Het Patel
#S2 CCC 2021
#17/02/20

rows=int(input())
columns=int(input())
num=int(input())

orders=[input().split() for i in range(num)]
orders=[(i[0], int(i[1])) for i in orders]

grid=[[-1 for j in range(columns)] for i in range(rows)]

for i in orders:
    if i[0]=='R':
        grid[i[1]-1]=[grid[i[1]-1][j]*-1 for j in range(columns)]

    if i[0]=='C':
        for row_num in range(rows):
            grid[row_num][i[1]-1]*=-1

count=0
for row in grid:
    count+=row.count(1)

print(count)
