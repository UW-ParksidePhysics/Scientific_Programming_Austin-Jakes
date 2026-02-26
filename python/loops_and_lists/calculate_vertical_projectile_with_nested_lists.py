times_positions = [[0.1,1.1,2.1].[0.1,0.5,2.2]]  # time, position

times = times_positions[0]

positions = times_positions[1]


times1 = [0,1,2,3]    # seconds
acceleration = 1    #m/s^2

positions1 = [0.5 * acceleration*time*time for time in times1]  # list comprehension

print(f'{positions1}')
