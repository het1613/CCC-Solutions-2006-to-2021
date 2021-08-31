#Global Warming J4 CCC 2010
#Het Patel
#ICS4U0
#9/19/20

while True:
    seq=input()

    if seq=='0':
        break

    seq=seq.split(' ')

    if seq[0]=='1':
        print('0')
        
    else:

        seq=[int(element) for element in seq]

        seq.pop(0)

        length=len(seq)-1

        differences=[]

        for current_diff in range(length):
            differences.append(seq[current_diff+1]-seq[current_diff])
        
        pattern=1

        while True:
            term=0

            while True:
                if (((term+pattern)>(len(differences)-1)) or (differences[term]!= differences[term+pattern])):
                    break
                term+=1

            if ((term+pattern)>(len(differences)-1)):
                break

            pattern+=1

        print(pattern)
