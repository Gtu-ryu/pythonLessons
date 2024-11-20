#1
import re

a=input('enter string')
while a!='':
  if re.fullmatch(r'[А-Я]\d{3}[А-Я]{2}\d{2,3}',a):
    print('Car')
  elif re.fullmatch(r'[А-Я]{2}\d{4,5}',a):
    print('Taxi')
  else:
    print('no valible')
  a=input('enter string')

#2
import re

with open('text.txt', 'r', encoding='utf-8') as file:
    b = file.readlines()
w = reduce(lambda x, y: x[:-1] + ' ' + y, b).split()
print(w)
fw = list(filter(lambda x: re.fullmatch(r'^[А-Яа-яёЁ]+[-]?[А-Яа-яёЁ]+[,.:]?', x) or re.fullmatch(r'^[A-Za-z]+[-]?[A-Za-z]+[,.:]?', x), w))
print(fw)
                  
#3
def change(txt):
    z = r'\b([01]?\d|2[0-3]):([0-5][0-9])(:([0-5][0-9]))?\b'
    r = re.sub(z, '(TBD)', txt)
    return r
c = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
g = change(c)
print(g)
#4
p='Владимир устроился на работу в одно очень важное место. И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО , ФГОУ ЧШУ АПК'
v=re.findall(r'\b[А-ЯЁ][А-ЯЁ]*[А-ЯЁ]\b',p)
print(v)
