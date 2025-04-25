n = int(input("Введите n: "))
m = int(input("Введите m: "))

mass = []

for i in range (0, n):
    mass.append([])
    for j in range (0, m):
        if i % 2 == 0:
            match j % 2:
                case 0:
                    mass[i].append('%')
                case 1:
                    mass[i].append('&')
        else:
            match j % 2:
                case 0:
                    mass[i].append('&')
                case 1:
                    mass[i].append('%')

mass[0][0] = '.'

for i in range(0, n):
    for j in range(0, m):
        print(mass[i][j], end=' ')
    print()