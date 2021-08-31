#Programmer: Het Patel
#Date Written: 01/17/20
#Version: A (Question 2)
#Purpose: Represent a line of text by "blocking" which means to compress the length of the block followed by the symbol in the back.

num_of_lines=int(input('Enter number of lines: ')) #Gets number of lines from user

all_lines=[] #Creates a list for all outputs at the end

for i in range(num_of_lines): #Creates a for loop for lines the user will enter
    text=input('Enter text: ') #Gets text from user for that line
    current_line=[] #This is a list that will hold all "blocks" in the current line
    
    position=0 #The current position of the line is at index 0
    
    while position<len(text)-1: #This creates a while loop which will only work while position is less than length of text
        char=text[position] #This will hold the current character of block
        counter=1 #This will hold how many times the character has been reapeated
        
        next_position=position+1 #This will check the character infront of the current character
        
        while char==text[next_position] and next_position!=len(text)-1: #Tis while loop determines how many times the current char has been reapated
            counter+=1 #If the next character is the same as current character, counter is incremented by 1
            next_position+=1 #This will check the character after the next character
            
        if next_position==len(text)-1 and char==text[next_position]: #This checks if the last character of the line has been met and if the last char is the same as current character
            counter+=1 #If so, counter is incremented
        
        current_line.append(str(counter)) #This appends the counter to current line
        current_line.append(str(char)) #This appends which character the block is
        
        if next_position==len(text)-1 and char!=text[next_position]: #If last character has been met, but the last char is not the same
            current_line.append(str(1)) #Then, append 1
            current_line.append(str(text[next_position])) #Append the last character (new block)
        
        position+=counter #After the block ends, the position is incremented by how many repeated characters there were
        
    all_lines.append(current_line) #This appends the current line to all lines

for i in all_lines: #This goes thorugh all lines in the list we made in the beginning
    print(' '.join(i)) #This joins current line with spaces

    
