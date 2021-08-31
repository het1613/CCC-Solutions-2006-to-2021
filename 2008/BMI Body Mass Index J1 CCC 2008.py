weight=float(input('Enter your weight in kg: '))
height=float(input('Enter your height in m: '))

BMI=(weight)/(height*height)

if (BMI>25):
    health='\nOverweight'
elif (BMI<18.5):
    health='\nUnderweight'
else:
    health='\nNormal weight'

print(health)
