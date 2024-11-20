#1)
s=0
try:
  n=int(input())
  if n >100:
    print('Превышен предел')
  for i in range(n):
    c=i**3
    s+=c
except ValueError :
  print('Не число')
print(s)
#2)
for i in range(1,10):
  for j in range(1,10):
    print('{:2d}'.format(i*j),end=' ')
  print('')
