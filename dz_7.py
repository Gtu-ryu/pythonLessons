#№1
import os

def print_docs(directory):
    if os.path.exists(directory):
        for item in os.listdir(directory):
            path = os.path.join(directory, item)
            print(path)
            if os.path.isdir(path):
                print_docs(path)
    else:
        print(f"Директория {directory} не существует.")

print_docs('gug')#вместо 'gug' - директория
#№2
def read_last(lines, file):
    abstract_file = open(file, 'r', encoding='utf-8')
    rows = abstract_file.readlines()
    for row in rows[lines:]:
        print(row)
a = 'article.txt'
n = int(input('Input int positive number: '))
file = open(a, 'r', encoding='utf-8')
rows_number = len(file.readlines())

if n > 0 and n < rows_number:
  read_last(n, a)
#№3
def longest_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    words = content.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
result = longest_words('article.txt')
print(result)  
#№4
def simple_text_editor():
    file_name = input("Введите имя будущего файла (без расширения): ")
    file_name += ".txt"
    print(f"Файл будет сохранен как {file_name}. Для завершения ввода введите пустую строку или символ.")
    with open(file_name, 'w') as file:
        while True:
            line = input("Введите строку: ")
            if line.strip() == "" or not line.isprintable():
                print(f"Файл '{file_name}' сохранен.")
                break
            file.write(line + "\n")
simple_text_editor()
