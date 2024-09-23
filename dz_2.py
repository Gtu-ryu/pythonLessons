1)
try :
    a=float(input('chisl '))
    b=float(input('znamen '))
    if b==0:
        print('Делить на ноль нельзя')
    else:
        print(a/b)
except ValueError:
    print('Введите число')

2)
a=0
try :
    a = float(input('Цена тпокупки '))
    if a>20:
        c=a*0.35
        a = a-c
        print(f'Цена со скидкой-{round(a,2)}, скидка-{round(c,2)}')
    else:
        print('bez skidki')
except ValueError:
    print('Введите число')

3)
a=int(input('1-12 '))
if a in range(1,13):
    if a in range(1,3) or a==12:
        print('winter')
        if a==1:
            print('january')
        elif a==2:
            print('february')
        else:
            print('december')
    elif a in range(3,6):
        print('spring')
        if a==3:
            print('march')
        elif a==2:
            print('april')
        else:
            print('may')
    elif a in range(6,9):
        print('summer')
        if a==3:
            print('june')
        elif a==2:
            print('jule')
        else:
            print('august')
    elif a in range(9,12):
        print('autum')
        if a==3:
            print('september')
        elif a==2:
            print('october')
        else:
            print('november')
