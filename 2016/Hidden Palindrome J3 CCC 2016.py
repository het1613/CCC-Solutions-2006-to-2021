def palindrome_checker(string): #this defines a new function called "palindrome_checker" which has one parameter
                                #the one parameter is a string that the function will check is a palindrom which is assigned to the varaible "string"
                                #the function will return a boolean value (True or False) and all the statements below are part of the function
                                
    normal=string #this assigns the varaible "string" to the variable "normal". The string is bacially duplicated.
    reverse=string[::-1] #this creates a new string which is the reverse of the varaible "string". This is done through splicing.
                         #splicing has 3 arguments, the first being an integer representing the starting index of the substring, in this case the default (0)
                         #the second being an integer representing the ending index of the substring, in this case the default (end of string)
                         #the last is an optional argumenht which is step, which skips n number of characters in the main string to create a substring
                         #in this case, instead of skipping, we are entering -1 which starts at the end and comes to the front without skipping any characters

    if (normal==reverse): #checks if variables normal and reverse are equal
        return True #if so, it means the string is the same forwards and in reverse meaning it is a palindrome. As such, the boolean value True is returned to wherever the function was called from in the main program.
    else: #the statment below is executed if the two varaibles are not equal
        return False #this means the string is not the same forwards and in reverse and is not a palindrome. As such, the boolean value False is returned to wherever the function was called from in the main program.

word=input('Enter a word: ') #asks the user to input a word which is stored as a string in the varaible "word"

longest_palindrome='' #creates an empty string which is assigned to the variable "longest_palindrome". We will use this variable to hold the longest possible palindrome. Since we have checked anything yet, string is empty

for start in range(len(word)): #creates a for loop which will repeat the statements below for the length of the varaible "word" times. the integer variable "start" represents the starting index of a possible palindrome which starts at 0 and ends 1 below the length of word, incrementing each time for loop is completed
    for end in range(len(word)): #creates a for loop which will repeat the statements below for the length of the varaible "word" times. the integer variable "end" represents the ending index of a possible palindrome which starts at 0 and ends 1 below the length of word, incrementing each time for loop is completed
        string=word[start:end+1] #a substring of the varaible word is created using splicing which is assigned to the variable "string"
                                 #splicing has 3 arguments, the first being an integer representing the starting index of the substring, in this case the varaible start
                                 #the second being an integer representing the ending index of the substring, in this case the varaible end
                                 #the last is an optional argumenht which is step, which skips n number of characters in the main string to create a substring
                                 #we do end+1 because the substring ends 1 below the ending index automatically so to account for that factor, we add 1 to the variable end
        
        if (palindrome_checker(string)): #checks if the boolean value returned from the function "palindrome_checker" is True
                                         #the function has 1 argument, a string (in this case the variable string" that the function will check is a palindrome or not
                                         #the return from the function is a boolean value (True or False)
            if (len(string)>len(longest_palindrome)): #if the substring is a palindrome, it then checks if the length of the substring (varaible string) is greater than the length of the longest palindrome (varaible longest_palindrome) we have found so far
                longest_palindrome=string #if so, the varaible "string" is now the longest palindrome we have found and the varaible "string" is assigned to the variable "longest_palindrome"

length=len(longest_palindrome) #length of the variable longest_paldindrome is found and assigned to the varaible "length"
                
print('The longest palindrome is "{0:s}" at {1:d} letters.'.format(longest_palindrome,length)) #the string varaible longest_palindrome and integer variable length are printed on the user's screen in an formatted output

    
    
