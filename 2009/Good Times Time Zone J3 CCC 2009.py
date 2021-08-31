def TimeZone(local,change):
    new_time=local+change

    if (new_time>2400):
        new_time-=2400
    elif (new_time<0):
        new_time+=2400

    if ((new_time%100)>=60):
        new_time=((new_time//100)+100)+((new_time%100)-60)

    return new_time

current_time=int(input('Enter time in Ottawa (Military 24 Hour Format): '))

time_list=[0,-300,-200,-100,0,100,130]
city_list=['Ottawa','Victoria','Edmonton','Winnipeg','Toronto','Halifax',"St. John's"]

print()

for pos in range(len(city_list)):
    new_time=TimeZone(current_time,time_list[pos])

    print('{} in {}'.format(new_time,city_list[pos]))
