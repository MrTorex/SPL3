def get_user_input(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        print("Введите строки (пустая строка — конец ввода):")
        while True:
            line = input()
            if line == '':
                break
            f.write(line + '\n')

def copy_lines_with_duplicate_words(source_file, target_file):
    with open(source_file, 'r', encoding='utf-8') as f1, open(target_file, 'w', encoding='utf-8') as f2:
        for line in f1:
            words = line.split()
            if any(words.count(word) >= 2 for word in set(words)):
                f2.write(line)

def find_word_with_most_digits(filename):
    max_digit_count = 0
    max_digit_word_index = -1
    word_counter = 0

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            for word in words:
                word_counter += 1
                digit_count = sum(char.isdigit() for char in word)
                if digit_count > max_digit_count:
                    max_digit_count = digit_count
                    max_digit_word_index = word_counter

    return max_digit_word_index

get_user_input('F1.txt')
copy_lines_with_duplicate_words('F1.txt', 'F2.txt')
result = find_word_with_most_digits('F1.txt')
print(f"Номер слова с наибольшим количеством цифр: {result}")