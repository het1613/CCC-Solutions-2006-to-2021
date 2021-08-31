def row_checker(target_sum,square): #This defines a function called "row_checker" that checks if all the rows in a 4 by 4 square have the same sum which has 2 parameters
                                    #The first parameter is an integer which is the sum all rows of the square should be which the function has assigned the variable "target_sum" to
                                    #The second parameter is a 2D list representing a 4 by 4 square of integers which is assigned to the varaible "square"
                                    #All the indented statements below are part of the function
    
    flag=True #Creates a new boolean varaible called "flag" and assigns True to it. We will use this variable to keep sure every row meets target_sum else we will make it false 
    
    for row in range(4): #Creates a for loop which repeats the statments below 4 times. The integer variable row starts at 0 and ends at 3, each time incrememnted by 1 when loop is completed
                         #"row" will represent the row number we are on in the 4 by 4 square
        
        row_sum=sum(square[row]) #This calculates the sum of the current row using the sum() function
                                 #The sum() function takes 1 mandatory argument, a list of integers, in this case square[row)num] which is the element/list in square at index row_num
                                 #The return of the sum() function is the sum of the list in its parameters which is assigned to the varaible "row_sum"

        if (row_sum!=target_sum): #checks if the integer value of row_sum is not equal to the integer value of target_sum
            flag=False #if row_sum is not equal to target_sum, it means the sum of all the rows are not all the same and the 4 by 4 square is not magic
                       #as such, the boolean varaible flag now becomes False
            break #there is no need to continue the loop anymore since we have confirmed the square is not magic so we will break/exit the loop

    return flag #This returns the boolean varaible flag back to wherever it was called from in the main program

def col_checker(target_sum,square): #This defines a function called "col_checker" that checks if all the rows in a 4 by 4 square have the same sum which has 2 parameters
                                    #The first parameter is an integer which is the sum all rows of the square should be which the function has assigned the variable "target_sum" to
                                    #The second parameter is a 2D list representing a 4 by 4 square of integers which is assigned to the varaible "square"
                                    #All the indented statements below are part of the function
    
    flag=True #Creates a new boolean varaible called "flag" and assigns True to it. We will use this variable to keep sure every column meets target_sum else we will make it false 

    for column in range(4): #Creates a for loop which repeats the statments below 4 times. The integer variable column starts at 0 and ends at 3, each time incrememnted by 1 when loop is completed
                            #"column" will represent the column number we are on in the 4 by 4 square

        col_sum=0 #creates an integer varaible col_num which is assigned the value 0. We will use this varaible to keep track of the current column's sum then compare with the first row's sum
        
        for row in range(4): #Creates a for loop which repeats the statments below 4 times. The integer variable row starts at 0 and ends at 3, each time incrememnted by 1 when loop is completed
                             #"row" will represent the row we are on in the 4 by 4 square
            
            col_sum+=square[row][column] #The integer variable col_sum is incremented by the integer at the row of the current column we are checking

        if (col_sum!=target_sum): #checks if the integer value of col_sum is not equal to the integer value of target_sum
            flag=False #if row_sum is not equal to target_sum, it means the sum of all the columns are not all the same and the 4 by 4 square is not magic
                       #as such, the boolean varaible flag now becomes False
            break #there is no need to continue the loop anymore since we have confirmed the square is not magic so we will break/exit the loop

    return flag #This returns the boolean varaible flag back to wherever it was called from in the main program
    

square=[] #Creates an empty list and assigns it to the variable "sqaure". We will use this list as a 2D list to hold our square

for row in range(4): #Creates a for loop which will repeat the statements below for 4 times (0 to 3). In the beginning, the integer varaible row is set to 0 and will increment by 1 each time the loop is completed
    row=input().split() #Asks the user to input the current row which will then be converted from a string to a list using the .split() function. The .split() function will take the string and split it at every white space. This list of strings is assigned to the varaible "row"
    row=[int(element) for element in row] #Using list comprehention, a new list is created by the for loop which goes through every string in the list row and converts it to an integer. This integer is added to the new list. After the for loop is done, the new list is assigned back to the same list variable "row"
    square.append(row) #Using the .append() function, the list "row" is added/appended to the back of list "square"

first_row_sum=sum(square[0]) #This calculates the sum of the first row in the square using the sum() function
                             #The sum() function takes 1 mandatory argument, a list of integers, in this case square[0] which is the first element/list in square at index 0
                             #The return of the sum() function is the sum of the list in its parameters which is assigned to the varaible "first_row_sum"

row_flag=row_checker(first_row_sum,square) #The function "row_checker" is called which has two arguments
                                           #The first argument is an integer value representing the sum of the first row in the sqaure, in this case the integer varaible first_row_sum
                                           #The second argument is a 2D list representing the 4 by 4 square of integers, in this case the list square
                                           #The function's job is to confirm whether or not all the rows in the 4 by 4 square have the same sum as the first row
                                           #The boolean output is assigned to the variable row_flag

col_flag=col_checker(first_row_sum,square) #The function "col_checker" is called which has two arguments
                                           #The first argument is an integer value representing the sum of the first row in the sqaure, in this case the integer varaible first_row_sum
                                           #The second argument is a 2D list representing the 4 by 4 square of integers, in this case the list square
                                           #The function's job is to confirm whether or not all the columns in the 4 by 4 square have the same sum as the first row
                                           #The boolean output is assigned to the variable col_flag

if (col_flag) and (row_flag): #checks if both boolean varaibles col_flag and row_flag are True
    print('Magic') #if so, the 4 by 4 square is a magic square and the string "Magic" is printed on the user's screen using the print() function
    
else: #if one or both of the boolean varaibles is false, the statment below is executed
    print('Not Magic') #the 4 by 4 sqaure is not magic and the string "Not Magic" is printed on the user's screen using the print() function
