name_file = input('Введите имя файла (Например: myfamily.txt): ')
num_line_file = int(input('Введите номер строки из выбранного файла (целое число): '))
file = open(name_file, 'r')
s = ''
result = ''

for line in file:
    s += line

strings = s.split()

for index in range(len(strings)):
    if index == num_line_file - 1:
        result = strings[index]
        break
    else:
        result = 'Строки под таким номером нет! Попробуйте еще раз.'

print(result)
