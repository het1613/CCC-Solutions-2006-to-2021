def BabyChecker(father,mother,baby):

    flag=True

    for gene in range(5):

        if flag:
            
            if (baby[gene] in 'ABCDE'): #for gene to be capital, at least one of one parent's alleles has to be capital
                
                flag= (mother[gene*2] in 'ABCDE') or (mother[gene*2+1] in 'ABCDE') or \
                      (father[gene*2] in 'ABCDE') or (father[gene*2+1] in 'ABCDE')

            elif (baby[gene] in 'abcde'): #for gene to be lower, at least one of each parents alleles has to be lower

                flag= ((mother[gene*2] in 'abcde') or (mother[gene*2+1] in 'abcde')) and \
                      ((father[gene*2] in 'abcde') or (father[gene*2+1] in 'abcde'))

    return flag

outputs=[]

father=input()
mother=input()

num_of_babies=int(input())

for iteration in range (num_of_babies):
    baby=input()

    if BabyChecker(father,mother,baby):
        status='Possible Baby.'
    else:
        status='Not their baby!'

    outputs.append(status)

print('\n'.join(outputs))

