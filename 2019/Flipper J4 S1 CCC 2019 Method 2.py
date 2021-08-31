grid=[['1','2'],['3','4']]

flips=input()

for current_flip in flips:
    if (current_flip=='H'):
        grid.reverse()
        
    elif (current_flip=='V'):
        grid[0].reverse()
        grid[1].reverse()

for row in range(len(grid)):
    print(' '.join(grid[row]))
