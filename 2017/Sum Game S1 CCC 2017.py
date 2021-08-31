def Same_Run(team1,team2,num): #This defines a function called "Same_Run" which takes 3 parametes. The first two are lists containing integers which are the number of runs scored for each team. The function names these lists team1 and team2
                               #The last parameter is an integer which is the number of games played by both teams. In this case, the function assigns the integer to the variable num

    max_same_run_game=0 #Creates a new integer variable max_same_run_game which is set to 0. We will use this to find the largest game number where the sum of the runs in all the previous games are the same

    for current_game in range(1,num_of_games+1): #Creates a for loop which repeats the statments below for a set number of times.
                                                 #The amount of times the loop will run is determined by its range. In this case, the integer varaible current_game will start at 0 and end at exactly num_of_games. At the end of each iteration, it will be incremented by 1.

        #This caculates the sum of all the runs scored in all the games uptil the current_game. This is done using splicing. We create a new list that contains the elements from index 0 to index 1 before the current_game from the teams full list (team1 and team2)
        #We then find the sum of this list using the sum() function which takes 1 list as an argument. The value returned by this function is assigned to a varaible associated with the team, in this case team1 and team2
        team1_sum=sum(team1[:current_game]) 
        team2_sum=sum(team2[:current_game])

        if (team1_sum==team2_sum): #Checks if the sum of all the runs scored in the games uptil current_game is equal for both teams (in other words, checks if the varaibls team1_sum and team2_sum are equal)
            max_same_run_game=current_game #if it is, then the current_game is so far the greatest game where the sum of all the runs scored in previous games is the same for both teams

    return max_same_run_game #Returns the integer value of max_same_run_game to wherever the function was called from in the main program


num_of_games=int(input()) #Asks the user to input the number of games played by the two teams which is converted from a string and stored as an integer in the varaible "num_of_games"

swifts=input().split() #Asks the user to input the number of runs in each game for the Swifts team which is a string. It is then converted to a list by splitting the string at white spaces and each element is the number of runs in a specific game as a string. (done using .split() function)
sema=input().split() #Asks the user to input the number of runs in each game for the Semaphore team which is a string. It is then converted to a list by splitting the string at white spaces and each element is the number of runs in a specific game as a string. (done using .split() function)

#Using list comprehention, the for loop goes through every game in the list and converts it from a string to an integer and appends it to a new list with the same name
swifts=[int(game) for game in swifts]
sema=[int(game) for game in sema]

max_same_run_game=Same_Run(swifts,sema,num_of_games) #Calls the function "Same_Run" which takes three arguments. The first two arguments are the lists containing the number of runs in each game as an integer for each team (in this case, swifts and sema). The last argument is an integer which is the number of games both teams have played (in this case, num_of_games)
                                                     #The integer value returned from the function is assigned to the varaible max_same_run_game

print(max_same_run_game) #The variable max_same_run_game is printed on the user's screen using the print() function

    

    
    
