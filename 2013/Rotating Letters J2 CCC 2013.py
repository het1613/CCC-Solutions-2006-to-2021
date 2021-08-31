word=input('Enter a word: ')
chars='HINOSXZ'

for letter in word:
    if letter not in chars:
        print('Not Rotatable')
        break
else:
    print('Rotatble')
