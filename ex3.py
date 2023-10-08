inp_file = open('input.txt', 'r')
out_file = open('simple/output.txt', 'w')
s = ''
for line in inp_file:
    s += line

string = s.split()

for line in string:
    if line[-1]:
        out_file.write(line[-1])
