tasks=[]
cant=[0 for i in range(11)]

tasks.append([1,7])
tasks.append([1,4])
tasks.append([2,1])
tasks.append([3,4])
tasks.append([3,5])

cant[7]=1
cant[4]=2
cant[1]=1
cant[5]=1

while True:
    before_task=int(input())
    after_task=int(input())

    if (before_task==0) and (after_task==0):
        break

    tasks.append([before_task,after_task])

    cant[after_task]+=1

index=0

order=['' for i in range(10)]

for i in range(1,8):
    for j in range(1,8):

        if (cant[j]==0):
            order[index]=str(j)
            index+=1
            cant[j]=-1

            for k in range(1,8):
                if ([j,k] in tasks):
                    tasks[tasks.index([j,k])]=[0,0]
                    cant[k]-=1

print()

if (index<7):
    print('Cannot complete these tasks. Going to bed.')

else:
    print(' '.join(order))
