#Question: Ragaman
#Programmer: Het Patel
#Teacher: Mr. Veera
#Course: ICS4U0
#Date: 10/01/20
#Purpose: To determine whether or not a given string is a wildcard anagram of another given string

def Possible_Anagram(word,anagram): #This defines the function Possible_Anagram which takes two parameters, word and anagram
                                    #The following indented statments are a part of this function

    used_letters='' #Creates an empty string and assigns it to the variable "used_letters". This variable will be used to hold all the characters in the string "word" that have been checked already
    possible_astricks=0 #Sets the variable "possible_astricks" to 0. We will use this varaible by incrementng it by the number of possible astricks we need for the string anagram to be an wildcard anagram of the string word

    status='N' #Sets the variable "status" to 'N' which means currently, the anagram is not a wildcard anagram of word. We will check if it is later and if so, we change the status later on

    for letter in word: #Creates a for loop which repeats the statements below for every letter in the string word
        if (letter not in used_letters): #Checks if the current letter the for loop is on was not already checked before by seeing if the letter is not in the string used_letters
            count_diff=word.count(letter)-anagram.count(letter) #Calculates the count of the letter in the string word and the string anagram then subtracts the anagram count from the word count of the letter
                                                                #The result is stored in the varaible count_diff
            if (count_diff<0): #Checks if count_diff is under 0
                break #If count_diff is under 0, it means that the letter appears in the anagram more than the word itself which is not possible if it is a wildcard anagram. It should only be the same or more in the word since some letters in the anagram are astricks
                      #As such, the loop is exited and status remains 'N'
            
            possible_astricks+=count_diff #If cound_diff is more than or equal to 0, it means the letter appears more pr the same in the word and there is a possibility that letter is a astrick in the anagram
                                          #So, the total number of astricks is incremented by the difference in count of the letter

            used_letters+=letter #Since we have checked this letter, in order to make sure we don't check it again, we add it to the varaible used_letters

    else: #The statments below are only run if the for loop was not broken and completly passed
        if (possible_astricks==anagram.count('*')): #checks if the value of possible_astricks is the same as the count of astricks in word
            status='A' #if it is, status is now changed to 'A' meaning it is a wildcard anagram of word
            #This works because if some letters are not present x amount of times in the anagram but the number of astricks is also x, the astricks can be those missing letters and it is an anagram

    return status #The varaible status is returned to the wherever the function was called in the main loop


word=input('Enter the word: ') #Asks the user to input the original word which is stored as a string in the variable "word"
anagram=input('Enter the anagram: ') #Asks the user to input the possible anagram which is stored as a string in the variable "anagram"

status=Possible_Anagram(word,anagram) #Calls the function Possible_Anagram which takes two arguments, both strings (word and anagram)
                                      #The output this fuction returns is stored in the varaible "status"
        
print(status) #The variable "status" is outputted on the user's screen using the print() function
