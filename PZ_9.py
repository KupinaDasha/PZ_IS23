#Выполнить сортировку словаря d = {'a': 1, 'b': 2, 'c': 3}
d = {'c': 3, 'a': 1, 'b':2}    #исходный словарь
sorted_dict = sorted(d.items())     #сортировка
print(dict(sorted_dict))    #Преобразование из списка в словарь