#Programmer: Het Patel
#Date: 9/17/20
#Version: 1.0
#Purpose: To output the appropriate quadrant depending on the given X and Y coordinates by the user

x_coordinate=eval(input('Give the X corrdinate: '))
y_coordinate=eval(input('Give the Y corrdinate: '))

if x_coordinate>0:
    if y_coordinate>0:
        quadrant_number=1
    elif y_coordinate<0:
        quadrant_number=4

elif x_coordinate<0:
    if y_coordinate>0:
        quadrant_number=2
    elif y_coordinate<0:
        quadrant_number=3

elif (x_coordinate==0) and (y_coordinate==0):
    quadrant_number='Origin'

print('\nQuadrant is: {}'.format(quadrant_number))
    
