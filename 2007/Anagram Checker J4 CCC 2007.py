first_phrase=input('Enter first phrase: ').lower()

second_phrase=input('Enter second phrase: ').lower()

used_letters=' '

status='\nIs an anagram'

for letter in first_phrase:
    
    if (letter not in used_letters):
        
        if (first_phrase.count(letter)!=second_phrase.count(letter)):
            status='\nIs not an anagram'
            break

        used_letters+=letter

print(status)

