result = ''

while True:
    try:
        name_file = input('Введите имя файла (Например: myfamily.txt): ')
        num_line_file = int(input('Введите номер строки из выбранного файла (целое число): '))
        file = open(name_file, 'r')
        break

    except FileNotFoundError:
        print('Файл с таким названием не найден. Попробуйте еще раз.')

lines = file.readlines()

for line in range(len(lines)):
    if line == num_line_file - 1:
        result = lines[line]

if num_line_file > len(lines) or num_line_file <= 0:
    result = 'Недопустимый номер строки'

print(result)
