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
