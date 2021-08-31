start=input()
start=start.split()
start=[int(element) for element in start]

end=input()
end=end.split()
end=[int(element) for element in end]

charge=int(input())

distance=abs(start[0]-end[0])+abs(start[1]-end[1])
#This finds out how many steps vertically and horizonatlly (sum)
#you have to move to get to your destination
#This distance is the bare minimum you have to travel to reach destination

status='N'

if charge>=distance: #You must have enough charge to move the minimum distance
    if (charge-distance)%2==0:
        #If you have left over charge which is an even number,
        #you can keep going staright then U-turn until all charge is done
        #This only works if differnce is even number, else you will not reach exact destination
        status='Y'
        
print(status)
    
    
    
