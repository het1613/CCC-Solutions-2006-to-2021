#Het Patel
#S1 CCC 2021
#17/02/20

n=int(input())
heights=[int(num) for num in input().split()]
bases=[int(num) for num in input().split()]

area=0
for i in range(n):
    area+=bases[i]*(heights[i]+heights[i+1])/2

print(area)
