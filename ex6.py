result = ''

while True:
    try:
        name_file = input('Введите имя файла (Например: myfamily.txt): ')
        file = open(name_file, 'r')
        num_line_file = int(input('Введите номер строки из выбранного файла (целое число): '))

        break

    except FileNotFoundError:
        print('Файл с таким названием не найден. Попробуйте еще раз.')
    except ValueError:
        print('Некорректно задан номер строки. Попробуйте еще раз.')

lines = file.readlines()

for line in range(len(lines)):
    if line == int(num_line_file) - 1:
        result = lines[line]

if int(num_line_file) > len(lines) or int(num_line_file) <= 0:
    result = 'Недопустимый номер строки.'

print(result)
