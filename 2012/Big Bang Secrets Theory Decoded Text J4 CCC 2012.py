#Question: Big Bang Secrets
#Programmer: Het Patel
#Teacher: Mr. Veera
#Course: ICS4U0
#Date Written: 10/1/20
#Purpose: To output a decoded version of the text inputted by the user depending on the amount to shift the characters by.

k_value=int(input('Value of K: ')) #Asks the user to input the k value which is stored as an integer in an integer variable called k_value. This will be used to determine how much to additionally shift each character by when decoding.

encoded_text=input('Encoded message: ') #Asks the user to input the encoded text/message which is stored as a string in a string variable called "encoded_text". This is the text our program will decode.

#Creates a list called "alpha" which holds each uppercase letter of the alphabet.
#This list will be used to determine the index of the characters in the string variable "text" as well as the new decoded character depending on its position in this list.
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

decoded_text='' #Creates a string variable called "decoded_text" which is set to an empty string. This variable will be used to hold the decoded version of the text entered by the user.

for letter_pos in range(len(encoded_text)): #Creates a for loop which repeats the statments below for every character position/index in the string variable "encoded_text" from 0 to length of text-1 (for loop automatically ends 1 before)

    index_of_old_char=alpha.index(encoded_text[letter_pos]) #Calculates the position/index of the current character in the text in the list "alpha" which is assigned to integer varaible "index_of_old_char"

    shift=(3*(letter_pos+1))+k_value #Calculates the amount of characters to shift backwards by doing 3 multiplied by original letter position+1)+k_value. This is the formula of decoding a character given in the question.
                                     #We do letter_pos+1 because index starts at 0 not 1 which means the first character in the encoded text would be index 0 in the text and in Python but for our purpose the first character should be index 1
    
    new_pos=index_of_old_char-shift #Creates a new integer variable called "new_pos" which holds the new position of the decoded character in the alphabet
                                    #The new position is calculated by subtarcting the integer variable "shift" from integer variable "index_of_old_char".
        

    if (new_pos<0): #Checks if the new position we calculated earlier is below 0
        new_pos+=26 #If it is, 26 is added to the integer variable "new_pos" to wrap it around to the back of the alphabet. If we don't do this, the new position would be a negative number which is still a valid index until a certain extent but for simplitiy sakes, we just add 26 to make all positions positive integers.  

    decoded_text+=alpha[new_pos] #The new character, determined by the character at the index of new_pos in the list "alpha", is added to the string variable "decoded_text"

print('\nDecoded Message:',decoded_text) #The string variable "decoded_text" is printed on the user's screen in a formatted output
                                             #'\n' in the beginning will ensure the output is printed after skipping a line
    
