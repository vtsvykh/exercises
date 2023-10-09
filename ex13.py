with open('input.txt', 'r', encoding='utf_8') as data:
    with open('output.txt', 'w', encoding='utf_8') as out_data:
        word_dict = {}
        text = data.read()
        words = text.split()
        for word in words:
            new_word = word.strip('!@#$%^&*()_+-="[]{}?><').lower()

            if new_word not in word_dict:
                word_dict[new_word] = 1
            else:
                word_dict[new_word] += 1

        s_dict = dict(sorted(word_dict.items()))

        for new_word in s_dict:
            out_data.write(new_word + ' ')
            out_data.write(str(s_dict[new_word]) + '\n')
