result = ''
data = open('input.txt', 'r')

try:
    string = data.readline().split()

    num_1 = int(string[0])
    num_2 = int(string[1])
    num_3 = int(string[2])

    result = num_1 / num_2 + num_3

except ValueError:
    result = 'Uncorrect'
except ZeroDivisionError:
    result = 'Dont devide by zero'

out_data = open('output.txt', 'w')
out_data.write(result)
