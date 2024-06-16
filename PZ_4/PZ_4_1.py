# Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
# целые степени числа A от 1 до N.
while True: #Обработак исключений
    try:
        a = float(input('Введите число:'))
        n = int(input('Введите степень:'))
        break
    except ValueError:
        print("Ошибка!")
i = 0
while i<n:
    i+=1
    print(a**i)