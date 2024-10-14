import math
m1=list(map(int,input().split()))
m2=list(map(int,input().split()))
m3=list(map(int,input().split()))
d=[m1,m2,m3]
def mcos(x,y):
  c=math.sqrt(x**2+y**2)
  return x/c
def myg(a,b,c):
  if abs(a)>abs(b):
    if abs(a)>abs(c):
      return 1
    else:
      return 3
  elif abs(b)>abs(c):
    return 2
  else:
    return 3
a1=mcos(m1[0],m1[1])
a2=mcos(m2[0],m2[1])
a3=mcos(m3[0],m3[1])
print(d[myg(a1,a2,a3)-1])

n= int(input())
def pali(a):
  c=str(bin(a))[2:]
  if c==c[::-1]:
    return True
  else: 
    return False
for i in range(n):
  if pali(i)==True:
    print(i)
