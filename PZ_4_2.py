# Дано целое число N (>0). Найти наименьшее целое положительное число K, квадрат
# которого превосходит N: K2 > N. Функцию извлечения квадратного корня не
# использовать.
while True: #Обработка исключений
    try:
        n = int(input('Введите число:'))
        k = 1
        break
    except ValueError:
        print("Ошибка!")
while k**2<=n:
    k+=1
print(k)