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
