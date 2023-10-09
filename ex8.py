with open('input.txt', 'r') as data:
    strings = data.readlines()

with open('input.txt', 'w') as data:
    for line in strings:
        if line.strip('\n') != '100':
            data.write(line)
