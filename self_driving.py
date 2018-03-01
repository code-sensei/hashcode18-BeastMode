# Filename
filename = 'a_example.in'
# Open file
file = open(filename, 'r')
# File_lines
file_lines = []
#  number of lines in file
num_lines = sum(1 for line in open(filename))

for line in file:
    file_lines.append(line);
    print(file_lines)


# initialize parameters
rows = file_lines[0].split(' ')[0]
coloums = file_lines[0].split(' ')[1]
no_of_vehicles = file_lines[0].split(' ')[2]
rides = file_lines[0].split(' ')[3]
bonus = file_lines[0].split(' ')[4]
steps = file_lines[0].split(' ')[5]

# vehicle parameters and ride planing
for index in range(1, len(file_lines)):
    steps_counter = 0
    vehicle_start_x = 0
    vehicle_start_y = 0
    start_x = file_lines[index].split(' ')[0]
    start_y = file_lines[index].split(' ')[1]
    dest_x = file_lines[index].split(' ')[2]
    dest_y = file_lines[index].split(' ')[3]
    earliest_start = file_lines[index].split(' ')[4]
    latest_finish = file_lines[index].split(' ')[5]

    # plan the ride
    steps_moved_x = int(start_x) - int(vehicle_start_x)
    steps_moved_y = int(start_y) - int(vehicle_start_y)
    steps_counter += steps_moved_x + steps_moved_y
    print('Steps: ' + str(steps_counter))