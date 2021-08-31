normal=input()
cipher_1=input()
cipher_2=input()

original_letters=[]
remapped_letters=[]
translated='\n'

for pos in range(len(normal)):
    
    if normal[pos] not in original_letters:
        
        original_letters.append(normal[pos])
        
        remapped_letters.append(cipher_1[pos])


for pos in range(len(cipher_2)):
    
    char='.'
    
    if cipher_2[pos] in remapped_letters:
        
        index=remapped_letters.index(cipher_2[pos])
        
        char=original_letters[index]

    translated+=char

print(translated)
        

