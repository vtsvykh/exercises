with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as out_file:
        info_file = file.read()

        upper_info_file = info_file.upper()

        out_file.write(upper_info_file)
