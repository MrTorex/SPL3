a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

try:
    print(a / b)
except ZeroDivisionError as e:
    print('Произошла ошибка:', e)
finally:
    print('До свидания!')