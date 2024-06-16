# В матрице найти минимальный элемент в предпоследнем столбце.
from random import randint

print("Пожалуйста, сделайте квадратную матрицу, чтобы программа работала корректно)")
x = int(input('Введите количество строк: '))
y = int(input('Введите количество столбцов: '))
A = [[randint(0, 100) for i in range(x)] for j in range(y)]

for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
        print(A[i][j], end = ' ')
    print()

minmatr = min([x[-2] for x in A])

print('Минимальный элемент предпоследнего столбца:', minmatr)