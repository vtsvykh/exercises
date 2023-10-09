with open('input.txt', 'r') as inp_file:

    with open('output.txt', 'w') as out_file:

        strings = inp_file.readlines()

        for line in strings:
            if line.strip('\n'):
                out_file.write(line.strip('\n')[-1])

