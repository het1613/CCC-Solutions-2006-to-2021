#Question: Zero That Out
#Programmer: Het Patel
#Teacher: Mr. Veera
#Course: ICS4U0
#Date Written: 10/1/20
#Purpose: To output the final sum of the integers read, after eliminating the previous integer when "zero" said by the boss

num_of_int=int(input('Enter the number of integers: ')) #Asks the user the number of integers that the boss will say which is stored as an integer in an integer variable called "num_of_int". This integer variable will be used to determine how many times our for loop runs later on.

all_int=[] #Creates an empty list called "all_int". This list will be used to hold all the valid integers the boss says later on.

for iteration in range(num_of_int): #Creates a for loop which repeates the statements below for num_of_int times
    
    num=int(input('Enter integer: ')) #Asks the user to input the integer the boss says which is stored as an integer in an integer varibale called "num"

    if (num!=0): #Checks if the integer varibale "num" is not equal to 0
        all_int.append(num) #If the statement above is True, "num" is appended/added to the list "all_num"

    elif ((num==0) and (len(all_int)!=0)): #Checks if the integer variable "num" is euqal to 0 and if the list "all_num" is not empty
                                           #We need to check if the list "all_int" is not empty because if it is, we cannot use the pop function to remove the last element (-1) as it will give an error if done on empty list
        all_int.pop(-1) #If the statement above is True, the last element/integer in the list "all_num" is removed

total_sum=sum(all_int) #The total sum is calcuated using the sum function and is stored in an integer variable called "total_sum"

print('\nThe total sum is {0:d}.'.format(total_sum)) #The integer variable "total_sum" is printed to the user's screen in a formatted output
                                                     #'\n' in the beginning will ensure the output is printed after skipping a line
