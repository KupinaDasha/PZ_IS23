# Открываем файл для чтения и выводим его содержимое на экранwith open('text18-14.txt', 'r') as file:
with open('text18-14.txt', 'r', encoding='utf-16') as file: 
    content = file.read() 
    print("Содержимое файла:") 
    print(content) 
 
# Подсчитываем количество пробельных символов 
num_whitespace = sum(1 for char in content if char.isspace()) 
print(f"Количество пробельных символов: {num_whitespace}") 
 
# Создаем новый файл и записываем текст в стихотворной форме, заменяя символы третей строки их числовыми кодами 
with open('text18-14_stih.txt', 'w', encoding='utf-16') as new_file:
    lines = content.split('\n') 
    for i, line in enumerate(lines): 
        if i == 2:  # если это третья строка 
            # Заменяем символы числовыми кодами 
            encoded_line = ''.join(str(ord(char)) for char in line) 
            new_file.write(encoded_line + '\n') 
        else: 
            new_file.write(line + '\n') 
 
print("Текст в стихотворной форме с символами третьей строки, замененными их числовыми кодами, записан в файл 'text18-14_stih.txt'.")