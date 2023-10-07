name_file = input('Введите имя файла (Например: myfamily.txt): ')
num_line_file = input('Введите номер строки из выбранного файла (целое число): ')

result = ''

try:
    file = open(name_file, 'r')
    strings = file.readlines()

    for index in range(len(strings)):
        if index == int(num_line_file) - 1:
            result = strings[index]
            break
        else:
            result = 'Строки под таким номером нет! Попробуйте еще раз.'

except FileNotFoundError:
    print('Файл не найден. Попробуйте еще раз.')

except ValueError:
    print('Некорректно задан номер строки. Попробуйте еще раз.')

print(result)
