import sys
M = int(input())
N = int(input())
grid = []

for i in range(M):
    temp = input().split(' ')
    grid.append([])
    for number in temp:
        grid[i].append(int(number))

#returns the coordinates of numbers that are products of a and b
def grid_coords(a, b):
    coordinates = []
    for i in range(M):
        for j in range(N):
            if grid[i][j] == a*b and not (i == M - 1 and j == N - 1):
                coordinates.append([i + 1, j + 1])
    return(coordinates)

#recursively applies grid_coords function to each node in tree
def solve(n):
    if n == [1,1]: 
        print('yes')
        sys.exit()
    else:
        temp = grid_coords(n[0], n[1])
        if temp==[]:
            print('no')
            sys.exit()
        for array in temp:
            solve(array)

print(solve([M,N]))
