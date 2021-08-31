#Programmer: Het Patel
#Date Written: 9/20/20
#Version: 1.0
#Purpose: To determine whether the given text is in English or French

num_of_lines=int(input('Enter number of lines: '))

t_count=0
s_count=0

for line in range(num_of_lines):
    text=input('Enter line of text: ')

    for letter in text:
        if ((letter=='t') or (letter=='T')):
            t_count+=1
        elif ((letter=='s') or (letter=='S')):
            s_count+=1

if (t_count>s_count):
    language='\nEnglish'
elif (t_count<=s_count):
    language='\nFrench'

print(language)
