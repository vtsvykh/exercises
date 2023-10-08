data = open('input.txt', 'r')
number = data.readlines()
data = open('input.txt', 'w').close()

for line in number:
    if line.strip('\n') != '100':
        new = open('input.txt', 'a')
        new.write(line)
