result = ''

while True:

    try:
        name_file = input('Введите имя файла (Например: myfamily.txt): ')
        with open(name_file, 'r') as file:
            num_line_file = input('Введите номер строки из выбранного файла (целое число): ')
            strings = file.readlines()

        for index in range(len(strings)):
            if 0 >= int(num_line_file) or int(num_line_file) > len(strings):
                print('Строки под таким номером нет. Попробуйте еще раз.')
                break
            else:
                if index == int(num_line_file) - 1:
                    result = strings[index]

        break

    except FileNotFoundError:
        print('Файл не найден. Попробуйте еще раз.')

    except ValueError:
        print('Некорректно задан номер строки. Попробуйте еще раз.')
        break

print(result)
