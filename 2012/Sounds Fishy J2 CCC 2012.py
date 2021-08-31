original_readings=[]

for current_reading in range(4):
    reading_value=int(input('Enter reading: '))
    original_readings.append(reading_value)

sorted_readings=original_readings[:]
sorted_readings.sort()

reversed_readings=original_readings[:]
reversed_readings.reverse()

if original_readings==reversed_readings:
    possibility='Fish At Constant Depth'
    
elif original_readings==sorted_readings:
    possibility='Fish Rising'
    
elif reversed_readings==sorted_readings:
    possibility='Fish Diving'
    
else:
    possibility='No Fish'

print(possibility)
    
