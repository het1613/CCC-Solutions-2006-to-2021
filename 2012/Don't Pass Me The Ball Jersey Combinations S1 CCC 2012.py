from math import factorial

jersey_number=int(input())-1

num_of_combinations=0

if (jersey_number>=3):
    num_of_combinations=int((factorial(jersey_number))/((factorial(jersey_number-3))*6))

print(num_of_combinations)
