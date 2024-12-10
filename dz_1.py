#1)
import math
r=int(input('Введите радиус окр в см '))
dlin=2*math.pi*r
s=math.pi*r**2
print(f'длинна окр {round(dlin,2)}')
print(f'Площадь окр {round(s,2)}')

#2)
x,y=10,55
print(f'x={x},y={y}')
x,y=y,x
print(f'x={x},y={y}')

#3)
import math
l=int(input('Введите длину маятника '))
g=9.81
t=2*math.pi*math.sqrt(l/g)
print(round(t,2))
