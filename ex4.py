name_file = input('Введите имя файла (Например: myfamily.txt): ')
num_line_file = int(input('Введите номер строки из выбранного файла (целое число): '))
file = open(name_file, 'r')
s = ''
result = ''

for line in file:
    s += line

strings = s.split()

for i in range(len(strings)):
    if i == num_line_file - 1:
        result = strings[i]
        break
    else:
        result = 'Ошибка'

print(f'Строка под номером {num_line_file} имеет вид: {result}')