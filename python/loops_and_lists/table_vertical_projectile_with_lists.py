
solid_objects = ['Earth', 'Moon']
gravitational_accelerations = [9.81, 1.63]  # m/s/s


initial_velocity = 5.  # m/s
number_of_times = 9

all_times = []
all_positions = []

for gravitational_acceleration in gravitational_accelerations:
 
    end_time = 2 * initial_velocity / gravitational_acceleration

    times = [index * end_time / number_of_times for index in range(number_of_times+1)]

    positions = [
        initial_velocity*time - 0.5*gravitational_acceleration*time**2 for time in times
        ]

    all_times.append(times)
    all_positions.append(positions)

print(f'For initial velocity of {initial_velocity:.2f} m/s:')
print(62*'-')

header_string = ''
for solid_object, gravitational_acceleration in zip(solid_objects, gravitational_accelerations):
    header_string = header_string + f'{solid_object:13} (g = {gravitational_acceleration:.2f} m/s/s) '
print(header_string)
print(62*'-')


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



