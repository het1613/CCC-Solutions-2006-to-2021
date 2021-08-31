#Programmer: Het Patel
#Date Written: 9/20/20
#Version: 1.0
#Purpose: To determine number of correct answers in a given set of student responses and answer key

num=int(input('Enter number of student responses: '))

responses=[input('Enter student response: ') for i in range(num)]
answers=[input('Enter answer: ') for i in range(num)]
counter=0

for pos in range(num):
    if (responses[pos]==answers[pos]):
        counter+=1

print('\nCorrect:',counter)


