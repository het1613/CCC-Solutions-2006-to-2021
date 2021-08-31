all_city_and_temp=[]

while True:
    user_input=input('Enter city and temperature: ').split()

    city=user_input[0]
    temp=int(user_input[1])

    all_city_and_temp.append([temp,city])

    if (city=='Waterloo'):
        break

all_city_and_temp=sorted(all_city_and_temp)

print(all_city_and_temp[0][1])
