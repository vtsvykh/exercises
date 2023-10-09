num = ''
result = ''
try:
    with open('input.txt', 'r', encoding='utf_8') as data:
        numbers = data.read().split()

        for element in range(len(numbers)):
            if numbers[element].isdigit():
                num += numbers[element]
                num += ' '

    num = num.split()[:3]
    data_1 = int(num[0])
    data_2 = int(num[1])
    data_3 = int(num[2])

    result = data_1 / data_2 + data_3


except ValueError:
    result = 'Недопустимое значение!'

except ZeroDivisionError:
    result = 'На ноль делить нельзя!'

with open('output.txt', 'w', encoding='utf_8') as out_file:
    out_file.write(str(round(result, 2)))
