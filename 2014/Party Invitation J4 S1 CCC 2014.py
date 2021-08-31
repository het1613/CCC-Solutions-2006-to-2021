num_of_friends=int(input('Enter number of friends: '))
num_of_rounds=int(input('Enter number of rounds: '))

friends_list=[str(friend_counter) for friend_counter in range(1,num_of_friends+1)]

for current_round in range(num_of_rounds):
    multiple=int(input('Enter multiple: '))

    counter=multiple-1
    
    while (counter<len(friends_list)):
        friends_list.pop(counter)
        counter+=multiple-1

print('\n'.join(friends_list))
