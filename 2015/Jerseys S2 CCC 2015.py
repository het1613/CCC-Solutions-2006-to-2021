num_of_jerseys=int(input())

num_of_players=int(input())

jerseys=[]
requests=[]
all_sizes='SML'

for number in range(1,num_of_jerseys+1):
    size=input()
    jerseys.append([all_sizes.index(size)+1,number])

for current_player in range(num_of_players):
    user_input=input().split()
    requests.append([all_sizes.index(user_input[0])+1,int(user_input[1])])

jerseys=sorted(jerseys)
requests=sorted(requests)

jersey_pos=0
counter=0

while (jersey_pos<num_of_jerseys-1):

    request_pos=0
    
    while (request_pos<num_of_players-1):
        
        if (jerseys[jersey_pos][0]>=requests[request_pos][0]):
            
            if (jerseys[jersey_pos][1]==requests[request_pos][1]):

                counter+=1

                jerseys.pop(jersey_pos)

                requests.pop(request_pos)

                break
            
        request_pos+=1
    else:
        jersey_pos+=1

print(counter)
