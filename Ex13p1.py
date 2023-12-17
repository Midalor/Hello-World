import random

# Создаем функцию для генерации случайной матрицы
def generate_matrix(rows, cols):
    matrix = []
    for j in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(-100, 100))  # Заполняем случайными значениями от -100 до 100
        matrix.append(row)
    return matrix

# Создаем две матрицы размерностью 10х10
matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

# Создаем третью матрицу и складываем значения из первых двух матриц
matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]

# Выводим результаты
print("Матрица 1:")
for row in matrix_1:
    print(row)
print()

print("Матрица 2:")
for row in matrix_2:
    print(row)
print()

print("Сумма матриц:")
for row in matrix_3:
    print(row)