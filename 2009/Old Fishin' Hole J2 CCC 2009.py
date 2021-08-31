trout_points=int(input('Enter Points For Brown Trout: '))
pike_points=int(input('Enter Points For Northern Pike: '))
pick_points=int(input('Enter Points For Yellow Pickerel: '))
max_points=int(input('Enter max points allowed: '))

print()

counter=0

for trout in range(max_points//trout_points +2):
    for pike in range(max_points//pike_points +2):
        for pick in range(max_points//pick_points +2):

            points=(trout*trout_points)+(pike*pike_points)+(pick*pick_points)

            if (points<=max_points) and (trout+pike+pick!=0):
                counter+=1
                print('{} Brown Trout, {} Northern Pike, {} Yellow Pickerel'.format(trout,pike,pick))

print('Number of ways to catch fish:',counter)         
