with open('input.txt', 'r') as data:

    with open('simple/output.txt', 'a') as out_data:
        strings = data.readlines()

        for line in range(len(strings)):
            if line % 2 != 0:
                out_data.write(strings[line])

