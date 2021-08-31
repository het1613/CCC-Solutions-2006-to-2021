#Algorithum Summary:
#We will create two lists of the bike speed of each citizen for the two countrys
#We will sort both lists from least to greatest

#If we have to find minimum total speed:
#the minimum total speed is found by pairing a citizen with the least bike speed from one country with another citizen with the least bike speed in that country
#then, find the largest bike speed out of the two citizens and move onto the next two least bike speed. We will do this from index 0 to the end of the lists

#If we have to find maximum total speed:
#the maximum total speed is found by pairing a citizen with the least bike speed from one country with another citizen with the greatest bike speed in that country
#then, find the largest bike speed out of the two citizens and move onto the next least and greatest bike speed. We will do this from index 0 to the end of the lists
#in order to do this, one of the lists should be reversed so that it is from greatest to least order


def Tandem_Bicycle(question,num,country1,country2): #This defines a new function called "Tandem_Bicycle" which has 4 parameters
                                                    #The first two parameters are integer values representing the question the function has to answer and the number of citizens (in this case, the function has assigned these values to the variables question and num respectively)
                                                    #The last two parameters are lists of integers representing the bike speeds of each citizen in each country (in this case the function has assigned the lists to varaibles country1 and country2 respectively)
                                                    #The function will return an integer value repsenting the total sum of all the max or min speed
                                                    #All indented statements below are part of this function

    if (question==2): #checks if the varaible question is equal to 2
        country2=country2[::-1] #if it is, it means we have to find the maximum speed. As such, we must reverse one of the country's lists, in this case country2
                                #we reverse the list using splicing. Splicing takes 3 arguments, start,end and step. In this case, start and end are kep default but step is -1 so a new list will be created by starting at the last element and working our way to the front without skipping
                                #this new list is assigned to the same variable country2

    total_speed=0 #Assigns the integer 0 to the varaible totla_speed. we will use this variable by incrementing the maximum speed between two citizens to find the total max/min speed

    for citizen in range(num): #This creates a for loop which will repeat the statements below for num times. The variable citizen starts at 0 and ends 1 before num, representing the current index of the citizen we are on
        total_speed+=max(team1[citizen],team2[citizen]) #total_speed is incremented by the max between the two bike speeds of the current citizens in country1 and country2 using the max() function
                                                        #in this case, we are only entering two arguments into the max() function but we could add more if we wanted to. The two arguments are integers representing the bike speed of the current citizen using the appropriate list and the variable citizen (our index value)
                                                        #the max() function will output the maximum value between the arguments enetered which in this case is used to increment total_speed by

    return total_speed #this returns the integer value of total_speed back to wherever the function was called from in the main program

    

question=int(input('Enter the type of question (1 or 2): ')) #Asks the user to input the question number which is converted from a string and stored as an integer in the variable question

num_of_citizens=int(input('Enter number of citizens: ')) #Asks the user to input the number of citizens in each country which is converted from a string and stored as an integer in the variable num_of_citizens

#Asks the user to input the bike speed of each citizen seperated by a whitespace for each country as a string which is then converted to a list using the .split() function
#The .split() function takes 1 argument, a substring (in this case, the default whitespace) that the function will seperate the string at (the string is the input from the user)
#The output from the function is assigned to the specific variable representing the country(either dmoj or peg)
dmoj=input('Enter bike speeds of citizens from Dmojistan: ').split() 
peg=input('Enter bike speeds of citizens from Pegland: ').split()

#Using list comprehention, each bike speed in each country's specific list is converted from a string to an integer
#The for loop in the square brackets goes through every element in the specific list. Each element is then converted to an integer and appended to a new list
#The new list then becomes the argument for the sorted() function which takes 3 arguments
#The first mandatory argument is a list of integers (in this case the one created using list comprehention)
#The other two arguments are key and a boolean argument reverse which we have not used
#The sorted() function will sort the list in accending order which is then assigned back to the variable for each country
dmoj=sorted([int(speed) for speed in dmoj])
peg=sorted([int(speed) for speed in peg])

total_speed=Tandem_Bicycle(question,num_of_citizens,dmoj,peg) #This calls the function "Tandem_Bicycle" which takes 4 arguments
                                                              #The first two arguments are integer values representing the question we have to answer and the number of citizens (in this case, the variable question and num_of_citizens)
                                                              #The last two arguments are lists of integers representing the bike speeds of each citizen (in this case the lists dmoj and peg)
                                                              #The function will return an integer value repsenting the total sum of all the max or min speed which is assigned to the varaiable total_speed

print(total_speed) #This prints the varaible total_speed to the user's screen using the print() function                                          

    
        

