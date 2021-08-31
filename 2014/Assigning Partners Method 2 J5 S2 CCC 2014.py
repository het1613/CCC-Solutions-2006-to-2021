num_of_students=int(input())

class_list_A=input().split()
class_list_B=input().split()

status='good'

for pos_1 in range(num_of_students):
    pos_2=class_list_A.index(class_list_B[pos_1])

    if (class_list_A[pos_1]!=class_list_B[pos_2]) or pos_1==pos_2:
        status='bad'
        break

print(status)
