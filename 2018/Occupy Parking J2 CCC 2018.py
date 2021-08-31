#Programmmer: Het Patel
#Date Written: 9/17/20
#Version: 1.0
#Purpose: To dtermine how many parking spots were occupied during both days.

def Occupy_Parking(day1,day2,num): #This defines a function called "Occupy_Parking" which has three parameters. The first 2 parameters are strings and sequences of two different parking records.
                                   #The thrid and last parameter is an integer determining the number of parking spots in the lot. In this case, the function gives it the name "num"
  counter=0 #This creates a new integer varaible called "counter" and assigns it the value of 0. We will use this varaible by incrementing it whenever a parking spot was occupied in both days

  for current_spot in range(num): #Creates a for loop which repeats the statements below for num_of_spots times. The integer variable "current_spot" starts at 0 and ends 1 below num_of_spots. We will use this varaible as an index marker.
    if ((day1[current_spot]=='C') and (day2[current_spot]=='C')): #checks if the parking spot in boht day1 and day2 was occupied using the current_spot varaible (which acts like an index value to determine which parking spot we are on)
      counter+=1 #If the parking spot was occupied both days, counter is incremented by 1

  return counter #This returns the value of counter to wherever the function was called from in the main program

num_of_spots=int(input('Enter number of parking spots: ')) #Asks the user to input the number of parking spots which is converted from a string and stored as an integer in the varaible "num_of_spots"
day1=input("Enter the record of yesturday's parking") #Asks the user to input the sequence of occupied and empty parking yesturday which is stored as a string in the variable "day1"
day2=input("Enter the record of today's parking") #Asks the user to input the sequence of occupied and empty parking today which is stored as a string in the variable "day2"

counter=Occupy_Parking(day1,day2,num_of_spots) #Calls the function "Occupy_Parking" and stores the integer value returned from the function in the varaible "counter"
                                               #The function takes three arguments, the first two are strings which are sequences of yesturdays and todays parking, in this case day1 and day2 and the thrid argument is an integer which is the total number of parking spots in the lot, in this case num_of_spots

print('{} parking spot(s) were taken both days.'.format(counter)) #Prints the varaible counter to the user's screen using the print() function in a formated output

