# Задание 2. Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ NºNº 2 - 9.


import tkinter as tk


def add_entry():
    # Добавляем новую строку с полями для ввода ключа и значения
    new_frame = tk.Frame(entries_frame)
    new_frame.pack(pady=5)

    new_key_label = tk.Label(new_frame, text="Ключ:")
    new_key_label.pack(side=tk.LEFT)

    new_key_entry = tk.Entry(new_frame, width=10)
    new_key_entry.pack(side=tk.LEFT)

    new_value_label = tk.Label(new_frame, text="Значение:")
    new_value_label.pack(side=tk.LEFT)

    new_value_entry = tk.Entry(new_frame, width=10)
    new_value_entry.pack(side=tk.LEFT)

    # Добавляем кнопку для удаления строки
    delete_button = tk.Button(new_frame, text="-", command=lambda: new_frame.destroy())
    delete_button.pack(side=tk.LEFT)


def sort_dict():
    # Собираем данные из полей ввода в словарь
    d = {}
    try:
        for child in entries_frame.children.values():
            if isinstance(child, tk.Frame):
                key = child.children["!entry"].get()
                value = int(child.children["!entry2"].get())
                d[key] = value
    except:
        result_field.insert(tk.END, "Ошибка, проверьте ввод.")

    # Сортируем словарь
    sorted_dict = dict(sorted(d.items()))

    # Выводим отсортированный словарь в текстовое поле
    result_field.delete("1.0", "end")
    result_field.insert(tk.END, str(sorted_dict))


# Создаем окно приложения
window = tk.Tk()
window.title("Сортировка словаря ПЗ №9")

# Добавляем кнопку для добавления строки
add_button = tk.Button(window, text="+", command=add_entry)
add_button.pack(pady=5)

# Создаем фрейм для полей ввода ключа и значения
entries_frame = tk.Frame(window)
entries_frame.pack()

# Добавляем 3 строки с полями для ввода ключа и значения
for i in range(3):
    add_entry()

# Добавляем кнопку для сортировки словаря
sort_button = tk.Button(window, text="Отсортировать", command=sort_dict)
sort_button.pack(pady=10)

# Создаем текстовое поле для вывода отсортированного словаря
result_field = tk.Text(window, width=30, height=10)
result_field.pack(pady=10)

# Запускаем главный цикл приложения
window.mainloop()
