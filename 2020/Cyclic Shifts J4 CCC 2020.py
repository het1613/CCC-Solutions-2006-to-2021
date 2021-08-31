def Cyclic_Shifts(text,old_string): #This defines a new function called "Cyclic_Shifts" which has 2 parameters
                                    #The first parameter is a string representing the main text we have to we have to find a cyclic shift within which in this case the function has assigned to the varaible "text"
                                    #The second parameter is also a string representing the string we will create cyclic versions of to mind in the main text which the function has assigned to the variable "old_string"
                                    #The return of this function a string, either 'yes' or 'no' representing if the main text contains a cyclic shift of old_string
                                    #All the indented statements below are a part of the function
    
    for cycle_count in range(len(old_string)): #creates a for loop which will repeat the statements below for the length of the varaible old_string times. The integer variable "cyclic_count" represents the current shift we are on which starts at 0 and ends 1 below the length of old_string, incrementing by 1 each time for loop is completed.                    

        new_string=old_string[1:]+old_string[0] #this statement will move the first character of 'old_string' to the back using splicing
                                                #this cyclic shift of old_string is assigned to the varaible 'new_string'
                                                #splicing has 3 arguments, the first being an integer representing the starting index of the substring, in this case the varaible start
                                                #the second being an integer representing the ending index of the substring, in this case the varaible end
                                                #the last is an optional argumenht which is step, which skips n number of characters in the main string to create a substring
                                                #for 'old_string[1:]' we are creating a substring from the character at index 1 of old_string to the end and adding character at index 0 of old_string to the back                

        if new_string in text: #checks if 'new_string' is in 'text'
            status='yes' #if it is, text contains a cyclic shift of the string 'old_string'. So, 'yes' is assigned to the varaiable 'status'
            break #since we have found a valid cyclic shift, we can break out of the for loop
        
        old_string=new_string #new_string is now assigned to old_string and we can repeat the process of moving the first character to the back again
        
    else: #the statement below is executed if the for loop is completed without breaking
        status='no' #this means 'text' does not contain a cyclic shift of 'old_string'. So, 'no' is assigned to the variable 'status'

    return status #this returns the varaible status back to wherever the function was called from in the main program

text=input('Enter text: ') #Asks the user to input some text which is stored as a string in the variable 'text'
string=input('Enter another text: ') #Asks the user to input another text which is stored as a string in the variable 'string'

status=Cyclic_Shifts(text,string) #This calls the function "Cyclic_Shifts" which takes 2 arguments
                                  #The first argument is a string where the cyclic shift is searched within (in this case, the varaible 'text')
                                  #The second argument is another string which we will create cyclic shifts of (in this casem the varaible 'string')
                                  #The function will return 'yes' or 'no' depending on whether text contains a cyclic shift of string
                                  #The string value returned from the function is assigned to the varaible status

print(status) #the variable status is printed to the user's screen using the print() function

    

    
    
