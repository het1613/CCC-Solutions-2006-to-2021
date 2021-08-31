#Programmer: Het Patel
#Date Written: 9/17/20
#Version: 1.0
#Purpose: To determine if a text message is sad or happy depending on the number of times the happy/sad emojis were used

def Happy_Emotion(text): #This defines a function called "Happy_Emotion" which has 1 paramter
                         #The parameter is a string that the function assigns to the varaible "text"
                         #The indeneted statments below are part of this function
    
    counter=text.count(':-)') #Given the string text, the .count() function has 1 mandatory parameter, a substring you would like to know the count of in the string text (in this case, ':-)"
                              #The other two optional parameters are integers start and stop which are the starting and ending indexes within the string where search starts 
                              #In this case, we are only enetring the mandatory parameter
                              #The return of this function is assigned to the variable "counter"
    
    return counter #This returns the integer value of counter to wherever the function was called from in the main program

def Sad_Emotion(text): #This defines a function called "Happy_Emotion" which has 1 paramter
                       #The parameter is a string that the function assigns to the varaible "text"
                       #The indeneted statments below are part of this function
    
    counter=text.count(':-(') #Given the string text, the .count() function has 1 mandatory parameter, a substring you would like to know the count of in the string text (in this case, ':-("
                              #The other two optional parameters are integers start and stop which are the starting and ending indexes within the string where search starts 
                              #In this case, we are only enetring the mandatory parameter
                              #The return of this function is assigned to the variable "counter"
    
    return counter #This returns the integer value of counter to wherever the function was called from in the main program

message=input('Enter a line of text: ') #Asks the user to input some text which is stored as a string in the varaible "message"

happy_counter=Happy_Emotion(message) #This calls the function "Happy_Emotion" which has 1 argument, a string, in this case the varaible message
                                     #The integer value returned from this function will be assigned to the variable "happy_counter"

sad_counter=Sad_Emotion(message) #This calls the function "Sad_Emotion" which has 1 argument, a string, in this case the varaible message
                                 #The integer value returned from this function will be assigned to the variable "sad_counter"

if (happy_counter>sad_counter): #checks if the integer variable happy_counter is greater than the integer varaible sad_counter
    emotion='Happy' #if it is, the emotion in the text is 'Happy" so "Happy" is assigned to the variable "emotion"
    
elif (happy_counter<sad_counter): #checks if the integer variable happy_counter is less than the integer varaible sad_counter
    emotion='Sad' #if it is, the emotion in the text is "Sad" so "Sad" is assigned to the variable "emotion"
    
elif (happy_counter==0 and sad_counter==0): #checks if the integer variable happy_counter and the integer varaible sad_counter are both equal to 0
    emotion='None' #if it is, the emotion in the text is "None" so "None" is assigned to the variable "emotion"
    
else: #the only other possibility remaining is that the integer variable happy_counter is equal to the integer varaible sad_counter
    emotion='Unsure' #if it is, the emotion in the text is "Unsure" so "Unsure" is assigned to the variable "emotion"

print(emotion) #This prints the string varaible emotion to the user's screen using the print() function
