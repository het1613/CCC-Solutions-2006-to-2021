#Programmer: Het Patel
#Date: 9/18/20
#Version: 1.0
#Purpose: To a output message for a "radar" sign that will show if the user is speeding and if so, what
#         their fine will be depending on the speed limit and recorded speed of the car given by the user

speed_limit=int(input('Enter the speed limit(km/h): '))
car_speed=int(input('Enter the recorded speed of the car(km/h): '))

speed_difference=car_speed-speed_limit #determines how much the driver was speding by over the limit

speeding=True

#Following if-statments determine the respective fine (if any) depending on the speed difference
if (speed_difference<=0):
    status='Congratulations, you are within the speed limit!'
    speeding=False

elif (speed_difference>=1) and (speed_difference<=20):
    fine=100

elif (speed_difference>=21) and (speed_difference<=30):
    fine=270

elif (speed_difference>=31):
    fine=500

if (speeding==False):
    print(status)
else:
    print('You are speeding and your fine is ${}.'.format(fine))
