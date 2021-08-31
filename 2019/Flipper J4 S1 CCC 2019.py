def grid_flipper(seq): #This defines a function called "grid_flipper" which takes one parameter, seq
                       #the parameter, seq, is a string consisting of some series of 'V' and 'H'
                       #All the indented statments below are a part of this function
    
    grid=[['1','2'],['3','4']] #Initializes the grid by creating a 2D list and assigning it to the varaible "grid". This will be the grid we will flip vertically and horizontally

    reduced_flips='' #Creates an empty string and assigns it to the variable "reduced_flips". This varaible will be used to hold "V", "H", or both instead of a long repeated sequence

    if (seq.count('V')%2==1): #checks if the count of 'V' in the original sequnce is odd by seeing if it is not divisible by 2 (if remainder of count/2 is 1)
        reduced_flips+='V' #If it is, the flips do not cancel out and the grid should only be flipped once vertically. So, 'V' is added to the varaible "reduced_flips".
                           #If the count was even (divisible by 2, R=0), the flips would cancel out. Doing a vertical flip and then a vertical flip again brings you back to the same initial position
        
    if (seq.count('H')%2==1): #checks if the count of 'H' in the original sequnce is odd by seeing if it is not divisible by 2 (if remainder of count/2 is 1)
        reduced_flips+='H' #If it is, the flips do not cancel out and the grid should only be flipped once horizontally. So, 'H' is added to the varaible "reduced_flips".
                           #If the count was even (divisible by 2, R=0), the flips would cancel out. Doing a horizontal flip and then a horizontal flip again brings you back to the same initial position
       
    if ('H' in reduced_flips): #checks if "H" is part of the string reduced_flips
        grid=grid[::-1] #If it is, the grid should be flipped horizontally which means the rows of the grid are switched.
                        #This can be done by reversing the entire grid so that the second row becomes the first and vis versa
                        #We reverve the grid using splicing ([::-1]) which creates a new list that goes starts from the back and comes to index 0. This new list is stored in the same variable grid
            
    if ('V' in reduced_flips): #checks if "H" is part of the string reduced_flips
        grid[0]=grid[0][::-1] #If it is, the grid should be flipped horizontally which means the rows of the grid are switched.
        grid[1]=grid[1][::-1] #This can be done by reversing the entire grid so that the second row becomes the first and vis versa
                              #We reverve the grid using splicing ([::-1]) which creates a new list that goes starts from the back and comes to index 0. This new list is stored in the same variable grid

    return grid #This returns the varaible grid back to wherever the function was called from in the main loop

flips=input('Enter sequence of flips: ') #Asks the user for a sequence of flips which is stored as a string in the varaible "flips"

grid=grid_flipper(flips) #Calls the function "grid_flipper" and assigns the value the function returns to the variable "grid"
                         #The function has 1 argument, a string consisting of some series of 'V' and 'H' called flips

for row in range(len(grid)): #Creates a for loop which repeats the statements below for every list in the list "grid" 
    print(' '.join(grid[row])) #Prints the current list onto the user's screen using the print() function
                               #the .join() function creates a string of the elements in the list in its parametes by joining them with one whitespace in between
