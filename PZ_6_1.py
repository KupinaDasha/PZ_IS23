#Дан список А размера N и целое число К (1 < К < N).
# Преобразовать список, увеличив каждый его элемент
# на исходное значение элемента Ак.

A = []
N = int(input('Введите размер списка: '))
K = int(input('Введите целое число: '))
for i in range(0, N):
    A.append(int(input('Введите число для списка: ')))
print(A)
AK = A[K-1]
for i in range(0, N):
    A[i] += AK
print(A)