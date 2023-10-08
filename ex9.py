data = open('input.txt', 'r')
out_data = open('simple/output.txt', 'a')

strings = data.readlines()

for line in range(len(strings)):
    if line % 2 != 0:
        out_data.write(strings[line])

data.close()
out_data.close()
