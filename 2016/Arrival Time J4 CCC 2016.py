#Programmer: Het Patel
#Date Written: 9/17/20
#Version: 1.0
#Purpose: To determine what the arrival time is depending on departure time and if rush hour is experienced

def Rush_Hour_Simulation(time): #This defines a new function called "Rush_Hour_Simulation" which has 1 parameter
                                #The parameter is an integer representing the departure time in minutes which in this case the function has assigned to the varaible time
                                #The return of this function is also an integer value representing the arrival time in minutes
                                #All the indented statements below are a part of the function
    
    distance=0 #Assigns the integer 0 to the variable distance. This varaible will represent the total distance we have travelled.
               #Currently we are at 0 because we have not started the simulation and our goal is 120 since it takes 120 minutes to arrive without rush hour
               #We assume we travel 1 unit without rush hour and 0.5 units in rush hour every minute

    while (distance<=119): #Creates a while loop which repeats the statements below while the value of varaible distance is less than or equal to 119
        time+=1 #If the while loop condition is met, we have not reached our destination and 1 minute is added to our time. We show this by incrementing the variable time by 1
                
        if ((time>=420 and time<=600) or \
            (time>=900 and time<=1140)): #Checks if the current time is within rush hour. We do this by checking if time is greater or equal to 420 (7 am in minutes) but less than or equal to  600 (10 am in minutes)
                                         #or if time is greater or equal to 900 (3 pm in minutes) but less than or equal to  1140 (7 pm in minutes)
            
            distance=distance+0.5 #if we are in rush hour, we only travel 0.5 units (half the distance we would normally travel in 1 minute)
                                  #so, distance is incremented by 0.5
            
        else: #the statement below is executed if the time is not within rush hour
            distance=distance+1 #since we are not in rush hour, we will travel the normal distance in 1 minute which is 1 unit
                                #so distance is incremenetd by 1

    return time #at the end of the simulation, the varaible time (integer representing arrival time in munutes) is returned to wherever the function was called from in the main program.

departure_time=input('Enter departure time: ').split(':') #Asks the user to input the departure time which is then converted from a string to a list using the .split() function
                                                          #The .split() function takes 1 argument, a substring (in this case, ':') that the function will seperate the string at (the string is the input from the user)
                                                          #The output from the function is assigned to the variable departure_time

departure_hour=int(departure_time[0]) #Converts the first element of the list departure_time from string to integer and assigns it to the varaible departure_hour
departure_min=int(departure_time[1]) #Converts the second element of the list departure_time from string to integer and assigns it to the varaible departure_min

departure_time=(departure_hour*60)+departure_min #Converts the time from 24-hour to minutes by multiplying number of hours by 60 minutes and adding the minutes to it
                                                 #The integer answer from the calculation is assigned to the variable departure_time 

arrival_time=Rush_Hour_Simulation(departure_time) #This calls the function "Rush_Hour_Simulation" which takes 1 argument
                                                  #The argument is an integer representing the time in minutes (in this case, the variable departure_time)
                                                  #The function will return what time in minutes Fiona will arrive from her normal 2h commute depending on the time she left at
                                                  #The integer value returned from the function is assigned to the varaible arrival_time

arrival_hour=(arrival_time//60)%24 #To convert back to 24-hour time, the hour is found by whole dividing arrival_time by 60, then finding the remainder when divided by 24
                                   #We do mod 24 to ensure the hour is under 24 if the communte has gone into the next day
                                   #The integer answer from the calculation is assigned to the variable arrival_hour

arrival_min=arrival_time%60 #We then find the minutes in the 24-hour time by doing arrival_time mod 60 which gives us the remaining minutes
                            #This integer answer from the calculation is assigned to the variable arrival_min

print('Arrival time is {0:02d}:{1:02d}.'.format(arrival_hour,arrival_min)) #This prints the varaibles arrival_hour and arrival_min to the user's screen using the print() function in a formatted output
                                                                           #We do {:02d} to ensure we have two leading zeros in front of the hour and time if there are no digits taking up the tens and ones place
