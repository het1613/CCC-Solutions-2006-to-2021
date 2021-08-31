#Question: GPS Text Entry
#Programmer: Het Patel
#Teacher: Mr. Veera
#Course: ICS4U0
#Date: 10/01/20
#Purpose: To output the total number of clicks needed to enter a waypoint into a GPS 

def Steps_Tracker(text): #This defines a new function called "Step_Tracker" which has one parameter, text. The statements below this are part of the function.
                         #The function will determine how many clicks it will take to enter the given text into the GPS and return that value to back to the main code

    #The following four lines are four different lists named "row0" to "row1"
    #The four lists contain the characters of the four rows on the GPS
    row0=['A','B','C','D','E','F']
    row1=['G','H','I','J','K','L']
    row2=['M','N','O','P','Q','R']
    row3=['S','T','U','V','W','X']
    row4=['Y','Z',' ','-','.','ENTER']

    keyboard=[row0,row1,row2,row3,row4] #This creates a 2D list of all the rows of the keyboard and assigns this 2D list to the list "keyboard"
                                        #The list keyboard just holds four more lists within it

    counter=0 #Sets the integer variable counter to 0 which we will use by incrementing it by the number of clicks takes for each letter to be entered into the keyboard

    old_x=0 #Sets integer variable old_x to the current x position of the cursor to 0
    old_y=0 #Sets integer variable old_y to the current y position of the cursor to 0

    for char in text: #Creates a for loop which repeats the statments below for every character in the string varaible "text"
        for row in keyboard: #Creates a for loop which repeats the statments below for every row in the list "keyboard"
            if char in row: #Checks if the current character the first for loop is on is in the list "row"
                new_x=row.index(char) #If it is, the new x position of the cursor will be the index of the character in the list "row"
                new_y=keyboard.index(row) #also, the new y position of the cursor will be the index of the list "row" in the list "keyboard"
                break #Since we know the x and y positions of the character, we can exit out of the second loop using break and finsih the first loop
            
        counter+=abs(new_x-old_x)+abs(new_y-old_y) #The number of clicks it will take to go to the character is determined by the sum of the absolute value of (new_x-old_x) and the absolute value of (new_y-old_y)
                                                   #We can find the absolute value of an expression by using the abs() function which takes 1 argument, a number to find the absolute value of

        old_x=new_x #Since we have reached our new character, the value of old_x is now set to the value of new_x 
        old_y=new_y #and the value of old_y is set to the value of new_y.

        #Now we move onto the next character in the text

    counter+=abs(4-old_y)+abs(5-old_x) #After all the characters in text have been entered, we have to press the "ENTER" button to set the waypoint in the GPS
                                       #This means we must account for the clicks it takes to go to the ENTER key which has x,y position of (5,4)
                                       #We use the same formula to determine the number of clicks it takes to go to a character as before but instead of new_x and new_y, the x and y positions of the ENTER key are hardcooded into the formula  
    return counter #This returns the integer varaible "counter" back to where the function was called from in the main loop. In this case, the value of counter is assigned to the integer varaible "steps" in the main code.


waypoint=input('Enter waypoint: ') #Asks the user to input the waypoint they would like to enter in the GPS. This inoput is stored as a string in the string variable "waypoint"

steps=Steps_Tracker(waypoint) #This calls the function "Steps_Tracker" which takes one argument, a string varaible waypoint.
                              #The value the function returns will be stored in the variable "steps" which is the total amount of clicks needed to enter the waypoint

print(steps) #Prints the varaible "steps" to the user's screen using the print() function

