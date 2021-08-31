#Programmer: Het Patel
#Date: 9/17/20
#Version: 1.0
#Purpose: To output the type of traingle depending on the angles given by the user

angle_A=int(input())
angle_B=int(input())
angle_C=int(input())

if (angle_A==angle_B==angle_C==60):
    triangle_type='Equilateral'

elif (angle_A+angle_B+angle_C==180):
    if ((angle_A!=angle_B) and (angle_A!=angle_C) and (angle_B!=angle_C)):
        triangle_type='Scalene'
    else:
        triangle_type='Isosceles'

else:
    triangle_type='Error'

print(triangle_type)
