#Question: Time on Task
#Programmer: Het Patel
#Teacher: Mr. Veera
#Course: ICS4U0
#Date: 10/01/20
#Purpose: To output the max number of chores the user can do in the given time

def Max_Chores_Calculator(chores,max_time): #This defines the function "Max_Chores_Calculator" (everything beneath it is part of the function). It has on parameter which is the list "chores". This list holds the time it takes to complete each chore.
    chores=sorted(chores) #This sorts the list "chores" in acending order using the sorted() function which needs one argument, a list. We are not providing the sorted() function with a key or if reverse is True

    max_chores=0 #This sets the integer varaible "max_chores" to 0. We will use this as a position tracker and a counter where we increment this variable by 1 if a chore is possible in the given time.
    time_taken=0 #This sets the iteger variable "time_taken" to 0. We will use this variabel to see how much time we have used up doing chores.

    while (time_taken+chores[max_chores]<=max_time): #This creates a while loop which repeats the statements below while the sum of time_taken and the time to do the next chore is under or equal the max_time allowed
        time_taken+=chores[max_chores] #If the condition above is True, the next chore can be done and the time_taken varaible is incrmeented by the time it takes to do that chore
        max_chores+=1 #Since we have completed another chore in the given time, we will incrmenet the max_chore counter by 1

    return max_chores #This returns the integer varaible "max_chores" back to where it was called from in the main code



max_time=int(input('Enter time you have to finish chores: ')) #Asks the user to input the time they have to finish the chores which is converted from a string and stored as an integer in the integer variable "max_time"

num_of_chores=int(input('Enter number of chores: ')) #Asks the user to input the time the number of chores they have which is converted from a string and stored as an integer in the integer variable "num_of_chores"

chores=[] #Creates an empty list and sets it to list variable "chores". This list will be used to hold the time it takes to complete each task (an integer)

for current_chore in range(num_of_chores): #Creates a for loop which repeats the statements below for num_of_chores times
    chore_time=int(input('Enter time to do chore: ')) #Asks the user to input the time it takes to finish the current chore which is converted from a string and stored as an integer in the integer variable "chore_time"
    chores.append(chore_time) #This adds/appends the integer variable "chore_time" to the list "chores" using the .append() function

max_chores=Max_Chores_Calculator(chores,max_time) #This calls the function "Max_Chores_Calculator" and the value the function returns is assigned to the integer variable "max_chores"
                                                  #This function has 2 arguments which are the list containing the time it takes to complete each chore and an integer variable which is the total amount of time the user has to complete the chores
                                                  #In this case, we are providing the function the list "chores" and integer varaible "max_time" as arguments

print('The maximum number of chores you can do is:',max_chores) #Outputs a sentence describing what is to follow and the integer variable "max_chores" using the print() function

