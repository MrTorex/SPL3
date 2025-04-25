jewelry = {
    "Кольцо": ["Серебро", 100, 15],
    "Бусы": ["Золото", 300, 10],
    "Серьги": ["Платина", 1000, 2]
}

def show_description():
    for key, val in jewelry.items():
        print(f"{key} - Состав: {val[0]}")

def show_price():
    for key, val in jewelry.items():
        print(f"{key} - Цена: {val[1]}")

def show_quantity():
    for key, val in jewelry.items():
        print(f"{key} - Количество: {val[2]}")

def show_all_info():
    for key, val in jewelry.items():
        print(f"{key} - Состав: {val[0]}, Цена: {val[1]}, Количество: {val[2]}")

def purchase():
    while True:
        key_name = input("Введите название изделия (или 'n' для выхода): ")
        if key_name == 'n':
            break
        if key_name in jewelry:
            quantity = abs(int(input("Введите количество: ")))
            if quantity <= jewelry[key_name][2]:
                total_price = quantity * jewelry[key_name][1]
                jewelry[key_name][2] -= quantity
                print(f"Вы купили {quantity} шт. {key_name} на сумму {total_price}. Осталось {jewelry[key_name][2]} шт.")
            else:
                print("Недостаточно товара на складе.")
        else:
            print("Такого изделия нет в магазине.")

def menu():
    choice = 0
    while choice != '6':
        print("Добро пожаловать в ювелирный магазин!\nВыберите пункт меню:\n1 - просмотреть описание\n2 - просмотреть цену\n3 - просмотреть количество\n4 - просмотреть всю информацию\n5 - покупка\n6 - выход")
        choice = input("Выберите пункт меню: ")
        
        match choice:
            case '1':
                show_description()
            case '2':
                show_price()
            case '3':
                show_quantity()
            case '4':
                show_all_info()
            case '5':
                purchase()
            case '6':
                print("До свидания!")
            case _:
                print("Неверный выбор. Попробуйте снова.")


menu()
