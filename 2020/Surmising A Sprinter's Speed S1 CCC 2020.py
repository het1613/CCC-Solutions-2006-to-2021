num_of_observations=int(input())

all_observations=[]

for current_observation in range(num_of_observations):
    observation_data=input().split()
    observation_data=[int(element) for element in observation_data]

    all_observations.append(observation_data)

all_observations=sorted(all_observations)

min_speed=0

for current_observation in range(len(all_observations)-1):
    time_elapsed=all_observations[current_observation+1][0]-all_observations[current_observation][0]
    distance=all_observations[current_observation+1][1]-all_observations[current_observation][1]

    speed=abs(distance/time_elapsed)
    
    if (speed>min_speed):
        min_speed=speed

print(min_speed)
