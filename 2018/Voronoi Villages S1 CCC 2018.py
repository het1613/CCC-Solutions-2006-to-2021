num_of_villages=int(input())

villages=[]

for current_village in range(num_of_villages):
    num=int(input())
    villages.append(num)

villages=sorted(villages)

village_sizes=[]

for current_village in range(1,len(villages)-1):
    right_most=(villages[current_village+1]+villages[current_village])/2
    left_most=(villages[current_village-1]+villages[current_village])/2
    
    current_size=right_most-left_most
    
    village_sizes.append(current_size)

print(round(min(village_sizes),1))
