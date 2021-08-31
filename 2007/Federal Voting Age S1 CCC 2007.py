num=int(input('Enter of birthdays to evaluate: '))

output=[]

for iteration in range(num):
    birthday=input('Enter birthday: ').split()

    year=int(birthday[0])
    month=int(birthday[1])
    day=int(birthday[2])

    status='No'

    if ((2007-year)>18):
        status='Yes'

    elif ((2007-year)==18):
        if (month<2):
            status='Yes'

        elif ((month==2) and (day<=27)):
            status='Yes'

    output.append(status)

print('\n'.join(output))
