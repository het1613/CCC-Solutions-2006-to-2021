N = input()
ways = [1,1,1,1,1,1,1]
for i in range(1,N):
    y = input()
    ways[y] = ways[y] * (1 + ways[i])

print(ways[N])
