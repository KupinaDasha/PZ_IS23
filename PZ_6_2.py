#Дан целочисленный список А размера N.
# Переписать в новый целочисленный список В
# того же размера вначале все элементы
# исходного списка с четными номерами,
# а затем — с нечетными:
# А2, А4, А6, ..., А1,  А3,  A4, ....
# Условный оператор не использовать.

import random
N = int(input('Размер списка: '))
ls1 = [random.randint(1, N) for i in range(1, N + 1)]
ls2 = ls1[0:len(ls1):2]
ls3 = ls1[1:len(ls1):2]
B = ls3 + ls2
print('список А: ', ls1)
print('список В: ', B)