# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.
while True: #Обработак исключений
    try:
        a = input('Введите слово:')
        break
    except:
        print("Ошибка!")
def ramka_2(a):
    i = 0
    while i < len(a) + 4:
        print('-', end='')
        i += 1
    print()
def ramka_1(a):
    ramka_2(a)
    i = 0
    while i<1:
        if i == 0:
            print('|'+' '+ a+' '+'|')
        else:
            print('|'+ (len(a)+2)*' '+'|')
        i+=1
    ramka_2(a)
ramka_1(a)