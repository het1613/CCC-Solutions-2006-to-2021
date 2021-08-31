num_of_students=int(input())

class_list_A=input().split()
class_list_B=input().split()

pairs=sorted([sorted([class_list_A[i],class_list_B[i]]) for i in range(num_of_students)])

status='good'

for current_pair in range(1,num_of_students,2):
    if (pairs[current_pair]!=pairs[current_pair-1]):
        status='bad'
        break

print(status)
        
