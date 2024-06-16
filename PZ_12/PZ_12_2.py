# Составить генератор (yield), который выводит из строки только цифры.
from string import digits

def stru(string):
    yield from [x for x in string if x in digits]
strin = 'В этом доме спрятано 4 ключа от 3 разных комнат, как вы поняли, 1 ключ не подходит ни к одной комнаты и нужен для дома номер 76 на улице 98'
str_1 = stru(strin)
print(list(str_1))