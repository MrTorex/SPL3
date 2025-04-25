def is_password_good(password):
    is_good = [0, 0, 0]
    
    if len(password) >= 8:
        is_good[0] = 1

    for i in password:
        if i.isupper():
            is_good[1] = 1

        if i.isdigit():
            is_good[2] = 1
        
        if all(is_good):
            return True
    
    return False

password = input("Введите пароль: ")

if is_password_good(password):
    print("Пароль хороший!")
else:
    print("Пароль плохой!")