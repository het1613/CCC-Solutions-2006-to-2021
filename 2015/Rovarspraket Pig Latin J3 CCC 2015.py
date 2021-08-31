def closest_vowel_finder(letter,letter_position): #This defines a function called "closest_vowel_finder" which has 2 parameters.
                                                  #The first parameeter is a string variable consisting of a single alpha character assigned to the varaible letter by the function
                                                  #The second parameter is an interger variable which is the index of the signle alpha character in the alphabet
                                                  #The indented statements below are a part of the function

    vowel_positions=[0,4,8,14,20] #Creates a list of all the integer positions of the vowels in the alphabet and assigns it to the list vowel_positions

    alphabet='abcdefghijklmnopqrstuvwxyz' #Creates a string with all the letters of the alphabet and assigns it to the varaible "alphabet"
    
    smallest_difference=26 #This assigns the variable "smallest_difference" the integer 26. We will use this variable to keep track of the smallest difference in index between the letter and a vowel

    for current_vowel_position in vowel_positions: #Creates a for loop which goes through all the integer elements in the list "vowel_positions". The integer element is assigned to the varaible "current_vowel_position"

        current_difference=abs(letter_position-current_vowel_position) #We find the current difference between the index of the letter in the alphabet and the current_vowel_position
                                                                       #We do this by finding the absolute value of letter_position-current_vowel_position using the abs() function which takes 1 argument, a number and returns the absolute value of it
                                                                       #We find absolute value because the cloest vowel can be before or after the letter. If we don't do absolute value we will only find the closest vowel behind the letter
                                                                       #The return from the abs() function is assigned to the variable current_difference

        if (current_difference<smallest_difference): #checks if the integer varaible current_difference is less than the integer varaible smallest_difference 
            smallest_difference=current_difference #if it is, the varaible smallest_difference now becomes the variable current_difference
            closest_vowel=alphabet[current_vowel_position] #and now the closest vowel we have found to the letter is the character at the current_vowel_position index in the string variable alphabet
                                                           #the string is assigned to the varaible closest_vowel

    return closest_vowel #returns the string varaible closest_vowel to wherever the function was called from in the main loop



def next_consonant_finder(letter,letter_position): #This defines a function called "closest_consonant_finder" which has 2 parameters.
                                                   #The first parameeter is a string variable consisting of a single alpha character assigned to the varaible letter by the function
                                                   #The second parameter is an interger variable which is the index of the signle alpha character in the alphabet
                                                   #The indented statements below are a part of the function

    vowel_positions=[0,4,8,14,20] #Creates a list of all the integer positions of the vowels in the alphabet and assigns it to the list vowel_positions

    alphabet='abcdefghijklmnopqrstuvwxyz' #Creates a string with all the letters of the alphabet and assigns it to the varaible "alphabet"
    
    next_consonant_position=letter_position+1 #the next possible consonant can be the position of the current letter in the alphabet +1
                                              #so, the varaible next_consonant_position is assigned the value of letter_position+1

    if (next_consonant_position in vowel_positions): #checks if the integer variable next_consonant_position is in the list of integers vowel_positions
        next_consonant_position+=1  #if it is, it means that the character at next_consonant_position in the alphabet is a vowel and not a consonant.
                                    #So we must increment the varaible next_consosnant_position by 1 which we know cannot be a vowel as no vowels are next to each other in the alphabet

    if (next_consonant_position>=26): #checks if next_consonant_position is greater or euqal to 26
        next_consonant_position=25 #if it is, it is an invalid index and there is no character at that index in the alphabet.
                                   #so, the closest consonant becomes 'z' which has index of 25. Thus, 25 is assigned to next_consonant_position

    next_consonant=alphabet[next_consonant_position] #the next_closest_consonant is the character at index next_consonant_position in the string varaible alphabet
                                                     #the string is assigned to the variable next_consonant

    return next_consonant #Returns the string varaible next_consonant to wherever the function was called from in the main program
    


word=input('Enter a word: ') #Asks the user to enter a word which is stored as a string in the varaible "word". This will be the string we translate.

vowels='aeiou' #Creates a string with all the vowels of the alphabet in order and assigns it to the varaible "vowels"

alphabet='abcdefghijklmnopqrstuvwxyz' #Creates a string with all the letters of the alphabet and assigns it to the varaible "alphabet"

translated='' #Creates an empty string and assigns it to the varaible "translated". We will use this string by adding letters of the final translated word to it

for letter in word: #Creates a for loop which repeats the statements below for every character in the string varaible "word". The character the for loop is on is assigned to the string varaible "letter"

    translated+=letter #Since the translated word also retains the original characters, we add the varaibe letter to the variable translated
    
    if letter not in vowels: #checks if the letter is not a vowel

        #if the letter is not a vowel, we need to add the vowel and consonant closest to the letter to the translated word
        
        letter_position=alphabet.index(letter) #we first have to find the position of the letter in the alphabet and we do this by using the function .index() which takes a string and finds the index of the substring (given in its argument) in the string
                                               #in this case, it is finding the index of string varaible letter in the string varaible alphabet

        closest_vowel=closest_vowel_finder(letter,letter_position) #this calls the "closest_vowel_finder" function which takes two arguments, a string consisting of a single character and an integer which is the index of the character in the alphabet (in this case, the varaible letter and letter_position)
                                                                   #the string returned from the function is assigned to the varaible "closest_vowel"
        closest_consonant=next_consonant_finder(letter,letter_position) #this calls the "closest_consonant_finder" function which takes two arguments, a string consisting of a single character and an integer which is the index of the character in the alphabet (in this case, the varaible letter and letter_position)
                                                                        #the string returned from the function is assigned to the varaible "closest_consonant"
        
        translated+=closest_vowel+closest_consonant #the string varaible "closest_vowel" and "closest_cpnsonant" are added to the string varaible "translated"

print(translated) #This will print the varaible "translated" to the user's screen
        
        
        
