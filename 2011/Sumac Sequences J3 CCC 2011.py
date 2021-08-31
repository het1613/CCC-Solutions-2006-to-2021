first_term=int(input('Enter the first term: '))
second_term=int(input('Enter the second term: '))

seq=[first_term,second_term]

while True:
    third_term=seq[-2]-seq[-1]
    seq.append(third_term)

    if (third_term>seq[-2]):
        break

print('\nLength:',len(seq))
print('Sumac Sequence:',seq)
