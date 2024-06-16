#Даны три целых числа. Найти количество положительных и количество
#отрицательных чисел в исходном наборе.
while True:     #обработка исключений
    try:
        a = int(input('Введите целое число:'))
        b = int(input('Введите целое число:'))
        c = int(input('Введите целое число:'))
        break
    except ValueError:
        print("Ошибка")
pol = 0
otr = 0
while True:
    if a > 0:
        pol += 1
    elif a==0:
        print("Вы ввели 0")
        break
    else:
        otr += 1
    if b > 0:
        pol += 1
    elif b==0:
        print("Вы ввели 0")
        break
    else:
        otr += 1
    if c > 0:
        pol += 1
    elif c==0:
        print("Вы ввели 0")
        break
    else:
        otr += 1
    print(f"Положительных:{pol}\nОтрицательных:{otr}")
    break