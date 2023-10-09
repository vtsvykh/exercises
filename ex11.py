with open('input.txt', 'r') as data:
    with open('output.txt', 'w') as out_data:
        numbers = data.read().split()
        int_numbers = map(int, numbers)
        sort_int_numbers = sorted(int_numbers, reverse=True)

        for num in sort_int_numbers:
            out_data.write(str(num) + '\n')
