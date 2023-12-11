# Дан список размера N. Осуществить циклический сдвиг элементов списка вправо на
# одну позицию (при этом A1 перейдет в A2, A2 — в A3,..., AN — в A1).
from random import randint  #импортирование модуля рандомных чисел
while True:     #обработка исключений
    try:
        def shift(lst, steps):
            if steps < 0:
                steps = abs(steps)
                for i in range(steps):
                    lst.append(lst.pop(0))
            else:
                for i in range(steps):
                    lst.insert(0, lst.pop())
        N = randint(0, 10)
        A = [randint(1, 10) for i in range(N)]
        print("Наш список:")
        print(A)
        shift(A, 1)
        print("Список со сдвигом вправо:")
        print(A)
        break
    except:
        print('Ошибка!')