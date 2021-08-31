month=int(input('Enter the month: '))
day=int(input('Enter the day: '))

if (month<2):
    status='Before'
elif (month>2):
    status='After'
elif (day<18):
    status='Before'
elif (day>18):
    status='After'
else:
    status='Special'

print(status)
