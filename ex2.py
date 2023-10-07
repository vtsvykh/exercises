file = open('input.txt', 'r')
out_file = open('output.txt', 'w')

for line in file:
    if line[0] == 'A' or line[0] == 'a':
        out_file.write(line)


