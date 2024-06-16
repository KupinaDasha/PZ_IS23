#Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж товаров торговой фирмы. 
#БД должна содержать таблицу Продажа товаров со 
#следующей структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.
import sqlite3
conn = sqlite3.connect('torg.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS sales(
                    sale_date DATE,
                   product VARCHAR(225),
                   amount INTEGER,
                   discount REAL,
                   filial VARCHAR(225),
                    manager VARCHAR(225)
)''')
conn.commit()

def input_data():
  data = []
  for _ in range(3):
    sale_date = input("Дата продажи: ")
    product = input("Товар: ")
    amount = float(input("Сумма: "))
    discount = float(input("Скидка: "))
    filial = input("Филиал: ")
    manager = input("Менеджер: ")
    data.append((sale_date, product, amount, discount, filial, manager))
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)", data)
  conn.commit()

def search_data():
  print("Варианты поиска:")
  print("1. По дате продажи")
  print("2. По товару")
  print("3. По филиалу")
  print("4. По менеджеру")
  change = input("Выберите вариант поиска: ")
  if change == '1':
    sale_date = input("Дата продажи: ")
    cursor.execute("SELECT * FROM sales WHERE sale_date=?", (sale_date,))
  elif change == '2':
    product = input("Товар: ")
    cursor.execute("SELECT * FROM sales WHERE product=?", (product,))
  elif change == '3':
   filial = input("Филиал: ")
   cursor.execute("SELECT * FROM sales WHERE filial=?", (filial,))
  elif change == '4':
   manager = input("Менеджер: ")
   cursor.execute("SELECT * FROM sales WHERE manager=?", (manager,))
  else:
    print("Неверный выбор")
    return
  res = cursor.fetchall()
  if res:
    for zapis in res:
      print(zapis)
  else:
    print("Записи нет")

def delete_data():
  print("Варианты удаления:")
  print("1. По дате продажи")
  print("2. По товару")
  print("3. По филиалу")
  print("4. По менеджеру")
  change = input("Выберите вариант удаления: ")
  if change == '1':
    sale_date = input("Дата продажи (ГГГГ-ММ-ДД): ")
    cursor.execute("DELETE FROM sales WHERE sale_date=?", (sale_date,))
  elif change == '2':
    product = input("Название товара: ")
    cursor.execute("DELETE FROM sales WHERE product=?", (product,))
  elif change == '3':
    filial = input("Филиал: ")
    cursor.execute("DELETE FROM sales WHERE filial=?", (filial,))
  elif change == '4':
    manager = input("Менеджер: ")
    cursor.execute("DELETE FROM sales WHERE manager=?", (manager,))
  else:
    print("Неверный выбор")
    return
  conn.commit()
  print("Записи удалены")

def update_data():
  print("Варианты редактирования:")
  print("1. По дате продажи")
  print("2. По товару")
  print("3. По филиалу")
  print("4. По менеджеру")
  change = input("Выберите вариант редактирования: ")
  if change == '1':
    sale_date = input("Дата продажи (для поиска записи): ")
    new_znach = input("Новое значение суммы продажи: ")
    cursor.execute("UPDATE sales SET amount=? WHERE sale_date=?", (new_znach, sale_date))
  elif change == '2':
    product = input("Название товара (для поиска записи): ")
    new_znach = input("Новое значение скидки: ")
    cursor.execute("UPDATE sales SET discount=? WHERE product=?", (new_znach, product))
  elif change == '3':
    filial = input("Филиал (для поиска записи): ")
    new_znach = input("Новое значение менеджера: ")
    cursor.execute("UPDATE sales SET manager=? WHERE filial=?", (new_znach, filial))
  elif change == '4':
    manager = input("Менеджер (для поиска записи): ")
    new_znach = input("Новое значение филиала: ")
    cursor.execute("UPDATE sales SET filial=? WHERE manager=?", (new_znach, manager))
  else:
    print("Неверный выбор")
    return
  conn.commit()
  print("Запись изменена")


while True:
  print("\nМеню:")
  print("1. Ввод данных")
  print("2. Поиск данных")
  print("3. Удаление данных")
  print("4. Редактирование данных")
  print("5. Выход")
  change = input("Выберите действие: ")
  if change == '1':
     input_data()
  elif change == '2':
    search_data()
  elif change == '3':
    delete_data()
  elif change == '4':
    update_data()
  elif change == '5':
    break
  else:
    print("Неверный выбор.")

conn.close()