data = open('input.txt', 'r')
out_data = open('output.txt', 'w')
numbers = data.readlines()

s = []

for line in numbers:
    num = int(line.strip('\n'))
    s.append(num)

so = sorted(s, reverse=True)

for i in so:
    out_data.write(str(i) + '\n')



