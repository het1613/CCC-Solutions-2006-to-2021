#Question: Silly Gym Game (Functions Test Question B)
#Programmer: Het Patel
#Teacher: Mr. Veera
#Course: ICS4U0
#Date Written: 07/10/20
#Purpose: To run a simulation of the game and output the winner, either Nikky or Byron or Tie


#This defines a new function called "UpandDown" which has 5 parameters
#The 5 parameters are all integer values representing the a, b, c, d and s values which the function as assigned to variables:
#nikky_forward, nikky_backward, byron_forward, byron_backward, and total_steps
#The return of this function a string indiciting the winner of the game, either 'Byron', 'Nikky' or 'Tie'
#All the indented statements below are a part of the function
def UpandDown(nikky_forward,nikky_backward,byron_forward,byron_backward,total_steps):

    #there are two parts to the function, a simulation for Nikky and a simulation for Byron
    #I will only comment for Nikky's simulation as Byron's simulation works in the same manner
    
    taken_steps=0 #so far Nikky has taken 0 steps as we have not started the simulation so 0 is assigned to varaible 'taken_steps'
    nikky_distance=0 #Nikky's position from the starting position is also 0 as we have started the simulation so 0 is assigned to varaible 'nikky_distaance'
    next_steps=nikky_forward #nikky will start by moving nikky_foward number of steps foward so the integer value of 'nikky_foward' is assigned to varaibale 'next_steps'
    change=1 #we are moving forward right now so change is assigned 1. When we move backwards, we will change this value to -1

    while (taken_steps+next_steps<=total_steps): #creates a while loop which will repeat the statements below for as long as nikky's current number of steps and the steps she will take does not surpass the total number of steps
        taken_steps+=next_steps #Nikky takes next_steps number of steps forward and taken_steps is incremented by that much
        nikky_distance+=next_steps*change #if Nikky is moving forward, next_steps would be nikky_forward steps and change would be 1. Thus, her distance from the starting position will be next_steps*1 and we will add that to nikky_distance
                                          #if Nikky is moving backwards, next_steps would be nikky_backward steps and change would be -1. Thus, her distance from the starting position will be next_steps*-1 and we will add that to nikky_distance
        
        if (change==1): #checks if change is equal to 1
            next_steps=nikky_backward #if so, nikky moved forward this round so the next round she will move backwards. Thus, next_steps becomes nikky_backward
        else:
            next_steps=nikky_forward #if she was moving backwards this round, she will move forwards next round. Thus, next_steps becomes nikky_foward 
            
        change*=-1 #Change is multiplied by -1. If chnage is initially -1, it will become 1, else it will become 1
        
    nikky_distance+=(total_steps-taken_steps)*change #Once we exit out of the while loop, Nikky still has some steps remaining to take
                                                     #we will find the remainign number of steps by doing total_steps-taken_steps and multiply it by chnage (indicates if she moves forward or backward)
                                                     #that valeu calculated is added to nikky_distance


    #the following simulation is the same as nikky's simulation but with different forward and backward values
    taken_steps=0
    byron_distance=0
    next_steps=byron_forward
    change=1

    while (taken_steps+next_steps<=total_steps):
        taken_steps+=next_steps
        byron_distance+=next_steps*change
        
        if (change==1):
            next_steps=byron_backward
        else:
            next_steps=byron_forward
            
        change*=-1
        
    byron_distance+=(total_steps-taken_steps)*change


    if byron_distance>nikky_distance: #checks if byron_distance is greater than nikky_distance
        winner='Byron' #if so, Byron is the winner and 'Byron' is assigned to variable winner
    elif byron_distance<nikky_distance: #checks if byron_distance is less than nikky_distance
        winner='Nikky' #if so, Nikky is the winner and 'Nikky' is assigned to variable winner
    else:
        winner='Tie' #else, if the distance is the same, it is a tie and 'Tie' is assigned to variable winner

    return winner #this returns the string value of winner back to wherever the function was called from in the main program

#The following 5 statments ask the user to input the values of a,b,c,d,s
#The inputs are converted from a string and stored as an integer in their respective variables
a_value=int(input('Given value for a: '))
b_value=int(input('Given value for b: '))
c_value=int(input('Given value for c: '))
d_value=int(input('Given value for d: '))
s_value=int(input('Given value for s: '))

#This calls the function "UpandDown" which takes 5 argument
#The 5 arguments are integers representing a,b,c,d,and s values
#The function will a string indicating the winner of the game
#The string value returned from the function is assigned to the varaible status
status=UpandDown(a_value,b_value,c_value,d_value,s_value) 

print() #prints empty line for spacing purposes
print(status) #prints the variable status to the user's screen using the print() function



