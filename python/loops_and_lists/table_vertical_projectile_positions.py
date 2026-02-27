# Table of t and y(t)
#
# y(t) = v0*t - (1/2)*g*t^2
#
# n + 1 uniformly spaced t values
# interval [0, 2*v0/g]


# pick two solid objects
solid_objects = ['Earth', 'Moon']
gravitational_accelerations = [9.81, 1.63]  # m/s/s

# pick positive initial velocity v0
initial_velocity = 5.  # m/s

# Set the number of intervals
number_of_times = 9

# Initialize the empty lists for all the times and positions
all_times = []
all_positions = []

for gravitational_acceleration in gravitational_accelerations:
    # End of the time interval
    end_time = 2 * initial_velocity / gravitational_acceleration

    # Calculate the times
    times = [index * end_time / number_of_times for index in range(number_of_times+1)]

    # Calculate the positions
    positions = [
        initial_velocity*time - 0.5*gravitational_acceleration*time**2 for time in times
        ]

    # Add the times and positions to the overall lists
    all_times.append(times)
    all_positions.append(positions)

# Print the table
print(f'For initial velocity of {initial_velocity:.2f} m/s:')
print(62*'-')

header_string = ''
for solid_object, gravitational_acceleration in zip(solid_objects, gravitational_accelerations):
    header_string = header_string + f'{solid_object:13} (g = {gravitational_acceleration:.2f} m/s/s) '
print(header_string)
print(62*'-')

# Make the column headers t (s) and y (m) for each object
column_headers = ''
column_underlines = ''
for index, solid_object in enumerate(solid_objects):
    column_headers += 4*' ' 
    column_headers += 't (s)'
    column_headers += 9*' '
    column_headers += 'y (m)'
    column_headers += 5*' '

    column_underlines += 4*' '
    column_underlines += 5*'-'
    column_underlines += 9*' '
    column_underlines += 5*'-'
    column_underlines += 5*' '
print(column_headers)
print(column_underlines)

for index in range(len(all_times[0])):
    row_values = ''
    for times, positions in zip(all_times, all_positions):
        row_values += f'{times[index]:9.3f}'
        row_values += f'{positions[index]:14.3f}'
        row_values += 5*' '
    print(row_values)

print(60*'_')
print(f'While Loop:')

index = 0
while index < number_of_times + 1:    
    row_values = ''
    
    row_values += f'{times[index]:9.3f}'
    row_values += f'{positions[index]:14.3f}'
    row_values += 5*''
    
    print(row_values)
    
    index += 1


