keyboard=['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

outputs=[]

while True:
    time=0
    
    word=input()
    
    if (word=='halt'):
        break

    for pos in range(len(word)):
        
        if (word[pos] in 'adgjmptw'):
            time+=1
            
        elif (word[pos] in 'behknqux'):
            time+=2
            
        elif (word[pos] in 'cfilorvy'):
            time+=3
            
        elif (word[pos] in 'sz'):
            time+=4

        if (pos>0):
            for group in keyboard:
                if ((word[pos-1] in group) and (word[pos] in group)):
                    time+=2
  
    outputs.append(str(time))

print('\n'.join(outputs))
