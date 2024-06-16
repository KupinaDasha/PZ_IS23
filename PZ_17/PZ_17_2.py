import os
import subprocess
import sys

# Задание 1

os.chdir('../PZ_11')
files = os.listdir()
print("Файлы в папке PZ_11: ")
for file in files:
    if os.path.isfile(file):
        print(file)

# Задание 2
os.chdir('../')
path = 'test/test1'
os.makedirs(path, exist_ok=True)

print("Папки test и test1 созданы.")

file_paths = {
    "./PZ_6/PZ_6_1.py": "./test/file1.txt",
    "./PZ_6/PZ_6_2.py": "./test/file2.txt",
    "./PZ_7/PZ_7_1.py": "./test/test1/test.txt"
}

for src, dest in file_paths.items():
    with open(src, "r") as src_file, open(dest, "w+") as dest_file:
        dest_file.write(src_file.read())
        print(f"Файл {src} скопирован в {dest}.")

total_size = 0
for root, _, files in os.walk('test'):
    for file in files:
        filepath = os.path.join(root, file)
        file_size = os.path.getsize(filepath)
        total_size += file_size
        print(f"Размер файла {file}: {file_size} байт")
print(f"Общий размер файлов {total_size} байт")

# Задание 3
os.chdir('PZ_11')
short_file = min(os.listdir(), key=len)
print("Файл с самым коротким именем:", short_file)


# Задание 4
os.chdir("../Отчеты")

report_filename = "PZ_5.pdf"

if sys.platform == "win32":
    subprocess.run(['start', report_filename], shell=True)
else:
    subprocess.run(['open' if sys.platform == "darwin" else 'xdg-open', report_filename])

# Задание 5
os.chdir('../test/test1')
files = [f for f in os.listdir() if os.path.isfile(os.path.join(os.getcwd(), f))]
print(*files)
os.remove('test.txt')
