# Filename
filename = 'a_example.in'
# Open file
file = open(filename, 'r')
# File_lines
file_lines = []

for line in file:
    file_lines.append(line);
    print(line)
