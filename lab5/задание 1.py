import numpy as np # type: ignore

#1
print("\nЗадание 1.1:\n")
vector = np.zeros(10)
print(vector)

#2
print("\nЗадание 1.2:\n")
vector = np.full(10, 2.5)
print(vector)

#3
print("\nЗадание 1.3:\n")
vector = np.zeros(10)
vector[4] = 1
print(vector)

#4
print("\nЗадание 1.4:\n")
vector = np.arange(10, 50)
print(vector)

#5
print("\nЗадание 1.5:\n")
arr = np.array([1, 2, 0, 0, 4, 0])
nonzero_indexes = np.nonzero(arr)
for i in nonzero_indexes:
    print(i, end=' ')
print('')

#6
print("\nЗадание 1.6:\n")
matrix = np.identity(3)
print(matrix)

#7
print("\nЗадание 1.7:\n")
random_array = np.random.rand(10, 10)
minimum_value = random_array.min()
maximum_value = random_array.max()
print("Массив со случайными значениями:")
print(random_array)
print("Минимальное значение:", minimum_value)
print("Максимальное значение:", maximum_value)

#8
print("\nЗадание 1.8:\n")
random_vector = np.random.rand(30)
mean_value = np.mean(random_vector)
print("Случайный вектор:")
print(random_vector)
print("\nСреднее значение всех элементов вектора:", mean_value)

#9
print("\nЗадание 1.9:\n")
matrix = np.zeros((8, 8))
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1
print(matrix)

#10
print("\nЗадание 1.10:\n")
matrix1 = np.random.rand(5, 3)
matrix2 = np.random.rand(3, 2)
result_matrix = np.dot(matrix1, matrix2)
print("Первая матрица (5x3):")
print(matrix1)
print("Вторая матрица (3x2):")
print(matrix2)
print("Результат умножения матриц (5x2):")
print(result_matrix)

#11
print("\nЗадание 1.11:\n")
array1 = np.random.rand(3)
array2 = np.random.rand(3)
print("Первый массив:", array1)
print("Второй массив:", array2)
if np.array_equal(array1, array2):
    print("Массивы равны.")
else:
    print("Массивы не равны.")

#12
print("\nЗадание 1.12:\n")
array = np.random.rand(5)
print("Исходный массив:", array)
max_index = np.argmax(array)
array[max_index] = 0
print("Массив после замены максимального элемента на 0:", array)

#13
print("\nЗадание 1.13:\n")
array = np.random.randint(0, 10, 20)
most_common_value = np.argmax(np.bincount(array))
print("Исходный массив:", array)
print("Наиболее частое значение в массиве:", most_common_value)

#14
print("\nЗадание 1.14:\n")
array = np.random.randint(0, 100, 20)
n = int(input("Введите n: "))
n_largest_values = array[np.argpartition(-array, n)[:n]]
print("Исходный массив:")
print(array)
print(n, " наибольших значения в массиве:")
print(n_largest_values)