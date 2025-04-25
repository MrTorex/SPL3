def func(input):
    if isinstance(input, list):
        m = 1
        for i in input:
            m *= i
        m = m ** (0.5)
        print("Среднее геометрическое: ", m)
    elif isinstance(input, dict):
        input = dict(sorted(input.items(), key=lambda x: x[1], reverse=True))
        print("Словарь был отсортирован по убыванию значения. Отсортированный словарь:  ", input)
    elif isinstance(input, int):
        for i in range(2, (input//2)+1):
            if input % i == 0:
                print("Введённое число не является простым!")
                return
        print("Введённое число является простым!")
    elif isinstance(input, str):
        temp = input.split()
        print("Количество слов в строке: ", len(temp))
        max_word = ""
        for i in temp:
            if len(i) > len(max_word):
                max_word = i
        print("Самое длинное слово: ", max_word)
    else:
        print("Введён неправильный тип данных!")

input1 = input("Введите список: ").split()
input1 = [int(num) for num in input1]
func(input1)

input2 = {}
length = int(input("Введите длину словаря: "))
print("Введите элементы словаря (вначале ключ, потом значение): ")
for element in range(0,length):
    input2[input()] = input()
func(input2)

input3 = int(input("Введите число: "))
func(input3)

input4 = input("Введите строку: ")
func(input4)