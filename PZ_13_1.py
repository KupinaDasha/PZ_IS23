#Для каждого столбца матрицы с четным номером найти
#сумму ее элементов
from random import randint

print("Пожалуйста, сделайте квадратную матрицу, чтобы программа работала корректно)")
x = int(input('Введите количество строк: '))
y = int(input('Введите количество столбцов: '))
A = [[randint(0, 100) for i in range(x)] for j in range(y)]

for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
        print(A[i][j], end = ' ')
    print()

rows = len(A)
cols = len(A[0])

for i in range(0, rows):
    if i % 2 != 0:
        sumCol = 0
        for j in range(0, cols):
            sumCol = sumCol + A[j][i]
        print("Сумма " + str(i + 1) + " столбца: " + str(sumCol))