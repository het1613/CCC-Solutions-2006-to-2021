def Sign_Creator(words,w): #This defines a new function called "Sign_Creator" which has 2 parameters
                           #The first parameter is a list of strings representing the words used in the sign which in this case the function has assigned to the varaible words
                           #The second parameter is an integer representing the width of the sign which in this case the function has assigned the variabe w to
                           #The return of this function is a 2D list of the sign (different rows to the sign)
                           #All the indented statements below are a part of the function
    
    full_sign=[] #creates an empty list that will hold the 2D list representing the sign
    
    while (len(words)>0): #creates a while loop which will repeat statements below while we have 1 or more elements in list 'words'

        row=[] #creates empty list which will hold current row of words

        #0 assigned to varaibles pos and length
        pos=0 #represents the index of the word we are on in the list 'words'
        length=0 #represents the length of the sign so far

        while ((pos<len(words)) and (length+len(words[pos])<=w)): #creates while loop which repeats statements below while 'pos' is less than length of list 'words' and length+the length of next word is less than the width
            row.append(words[pos]) #if True, the sign can hold the next word and is appended to the list sign
            length+=len(words[pos]) #the length of the sign so far is also incremented by the length of the word we just added

            pos+=1 #we increment pos by 1 to move onto next letter

            #we only add a '.' beside a word if there is another word following it. If there is no space left in the row, we do not need to add '.'
            if ((pos<len(words) and (length+1+len(words[pos])<=w))): #checks if pos is less than length of list 'words' and the length+1+the length of next word is less than width
                row.append('.') #if True, we append a '.' 
                length+=1 #length is also incremented by 1 since we added '.'
            else:
                break #if false, there is no space for the next word so we break out of the loop

        #if we have only 1 word in our row and there is space left but not enough to fit the next word, we still have to add a '.'
        if (len(row)==1) and (length!=w): #checks if length of sign is equal to 1 and length of the row is not equal to width
            row.append('.') #if true, we need to add '.' to sign
            length+=1 #we also need to add 1 to length

        words=words[pos:] #we reduce the list 'words' by removing the words we have already used in our sign. We do this by using splicing
                          #splicing has 3 arguments, the first being an integer representing the starting index of the new list, in this case pos
                          #the second being an integer representing the ending index of the new list, in this case the default (end of list)
                          #the last is an optional argumenht which is step, which skips n number of characters in the main list to create the new list
                          #the new list is asssigned to back to the same variable 'word'

        #we must add '.' for the remaining empty spaces we have left so we start at the first '.' in the sign and add another '.' to it.
        #Then we move onto the next '.' in the sign and add '.' to it and so on. When we reach the end of the list, we come to the front of the list again and start at the first '.'
        #continue doing so until we have no more spaces left
        #'.' in the list 'signs' are odd indexes so we can start at index 1 and add 2 to the index each time to move onto the next '.'

        remaining=w-length #the amount of remaining space we have left is the width minus length of the sign so far
        
        while (remaining>0): #creates a while loop which repeats the statements below while remaining is greater than 0
            for pos in range(1,len(row),2): #creates a for loop which goes through odd index elements in the list sign
                if (remaining<=0): #checks if remaining is equal or less than 0
                    break #if True, we do not have any more space left so we must break out of the for loop
                
                row[pos]+='.' #We add another '.' to the already exisisting '.'
                remaining-=1 #We have used up another space by adding a '.' so we reduce remaining by 1

        full_sign.append(row) #appends the current row of the sign to the 2D list full_sign

    return full_sign #this returns the 2D list full_sign back to wherever the function was called from in the main program
        
        
w=int(input('Enter w: '))#Asks the user to input the width which is then converted from a string and stored as an integer in the variable 'w'

words=['WELCOME','TO','CCC','GOOD','LUCK','TODAY'] #creates a list with all the words on the sign. Assigned to list 'words'

full_sign=Sign_Creator(words,w) #This calls the function "full_sign" which takes 2 arguments
                                #The first argument is a list of strings representing words to be used in the sign (in this case, the list words)
                                #The second argument is an integer representing the width of the sign (in this case, the variable w)
                                #The function will return a 2D list of the whole sign with width w with words equally distributed with spaces
                                #The 2D list returned from the function will be assigned to the varaible full_sign

for row in full_sign:
    print(''.join(row)) #the .join() method takes 1 parameter, a list of strings, which it converts into a string by joining them with some substring, in this case nothinh ('')
                        #the string returned from the .join() method is printed onto the user's screen using the print() function
