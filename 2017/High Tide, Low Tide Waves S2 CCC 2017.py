def Tide_Sorter(original_measurements,num): #This defines a new function called "Tide_Sorter" which has 2 parameters, a list containing integers of tide measurements which the function assigned to varaible "original_measurements"
                                            #and an integer that is the total number of measurements taken which the function assigns to the variable "num"

    correct_measurements=[] #This creates an empty list which is assigned to the varaible "correct_measurements". We will use this list by appending the actual order of tide measurements to it

    while (len(original_measurements)>0): #This creates a while loop which repeats the statements below while the length of the list "original_measurements" is more than 0. To avoid an infinite loop we remove elements from the list to decrease its length and have a break command within the loop

        if (len(original_measurements) == 1): #Checks if the length of the list "original_measurements" is equal to 1.
            correct_measurements.append(original_measurements[0]) # If it is, it is the last measurement left in the list "original_measurements" and can be added to the list "correct_measurements". The measurment will be the element at index 0 in original_measurements.
            break #Since all the measurements in the list "origianl_measurements" have been sorted in order, we can break/exit out of the loop

        #Since the low tides are always decreasing and high tides alway increasing, in the final order, we will see the largest tide followed by the smallest tide in the back
        #Then, the second largest and second smallest tide and so on. I tried to create this order with the algorithim below:

        #We find the maximum/minimum measurement by using the max() and min() function which takes a list as an argument and returns the greatest/least number in it
        max_measurement=max(original_measurements)
        min_measurement=min(original_measurements)
         
        #This will add/append the maximum/minimum measurement in original_measurements to the list correct_measurements.
        #We convert the maximum/minimum measurement to a string using the str() function and add it to the list correct_measturements using the .append() function
        correct_measurements.append(str(max_measurement)) 
        correct_measurements.append(str(min_measurement))

        #Since we have placed the minimum and maximum measurement in order and added it to our list correct_measurements, we can remove it from our origial_measurment list to avoid sorting it again and going into an infitite loop        
        #We can remove the maximum and minimum measurement by using the .remove() function which takes a list (in this case, original_measurements) and an argument which is an element to remove from the list (in this case, min_measurement and max_measurement)
        original_measurements.remove(max_measurement)
        original_measurements.remove(min_measurement)

    correct_measurements=correct_measurements[::-1] #This reverses the list correct_measurements using splicing. It will create a new list which starts at the last element in the list correct_measurements and comes to the first element
                                                    #This new list is then assigned back to the same variable correct_measurements

    return correct_measurements #This returns the list correct_measurements to wherever the function was called from in the main program

num_of_measurements=int(input()) #Asks the user to input the number of measurements they noted down which is converted from a string and stored as an integer in the varaible "num_of_measurements"
original_measurements=input().split() #Asks the user to input the sequence of scattered measurements which is originally a string but is then converted into a list by splitting the string at whhite spaces usign the .split() function.
                                      #The list is then assigned to the variable original_measurements

for pos in range(len(original_measurements)): #Creates a for loop which repeats the statments below for a set number of times determined by its range
                                              #the integer varaible pos a range that starts at 0 and ends at 1 below length of the list original_measurements. At the end of every iteration, pos is incremented by 1
                                              #everytime pos is within that range, the statments below are executed again
    
    original_measurements[pos]=int(original_measurements[pos]) #The string "measurement" which is an element in the list "original_measurements" is converted to an integer and assigned back to the sane varaible "measurement"

correct_measurements=Tide_Sorter(original_measurements,num_of_measurements) #This calls the function "Tide_Sorter" which takes 2 arguments, a list of integers containing the scattered tide measurements (in this case, the list "original_measurements") and an integer which is the number of total measurements taken (in this case, the variable num_of_measurements)
                                                                            #The list returned by the function is assigned to the varaible "correct_measurements"

print(' '.join(correct_measurements)) #The .join() function will return a string where all the string elements in the list inputted are joined by a single white space
                                      #This string returned by the .join() function will be printed to the user's screen using the print() function
