unopened=[100,500,1000,5000,10000,25000,50000,100000,500000,1000000]

num_of_opened=int(input('Enter number of opened briefcases: '))

for current_case in range(num_of_opened):
    case_number=int(input('Enter case number: '))
    unopened[case_number-1]=0

average_of_unopened=sum(unopened)/(len(unopened)-num_of_opened)

bankers_deal=int(input("Enter the Banker's offer: "))

status='\nno deal'

if (average_of_unopened<bankers_deal):
    status='\ndeal'

print(status)
