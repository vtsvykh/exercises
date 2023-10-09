with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as out_file:
        for line in file:
            if line[0] == 'A' or line[0] == 'a':
                out_file.write(line)


