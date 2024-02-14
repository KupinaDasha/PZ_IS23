# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс первого минимального элемента:
# Умножаем все элементы на минимальный элемент:
list = ['-3 18 8 -4 54 9']
file_1 = open('data_1.txt', 'w')
file_1.writelines(list)
file_1.close()

file_2 = open('data_2.txt', 'w')
file_2.write('Исходные данные: ')
file_2.write('\n')
file_2.writelines(list)
file_2.close()

file_3 = open('data_1.txt')
k = file_3.read()
k = k.split()
for i in range(len(k)):
 k[i] = int(k[i])
file_3.close()

mi=min(k)
minimum = (k.index(mi))

prois = " ".join(list)
prois = " ".join([str(int(x)*mi) for x in prois.split()])
f4 = open('data_2.txt', 'a') # открываем файл для дозаписи
f4.write('\n')
print('Количество элементов:', len(k),'\n' 'Индекс первого минимального элемента:', minimum, '\n' 'Умножаем все элементы на минимальный элемент:', prois,file=f4)
f4.close()