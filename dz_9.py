from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(-1, 2, 1000)
def f(x,a,b):
  y=(x**b+a**b)/(x**b)
  y[y>20]=np.nan
  y[y<-20]=np.nan
  return y
def gr1():
  a,b=1,1
  plt.plot(x,f(x,a,b),color='red' , markersize=0.5,label=f'A={a},B={b}')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('F(X)=x^b+a^b/x^b')
  plt.grid()
  a,b=2,1
  plt.plot(x,f(x,a,b),color='blue' , markersize=0.5,label=f'A={a},B={b}')
  a,b=1,2
  plt.plot(x,f(x,a,b),color='green' ,markersize=0.5,label=f'A={a},B={b}')
  plt.legend()
  plt.show()
gr1()
def gr2():
  x = np.linspace(0, 5, 1000)
  a,b=1,1
  plt.plot(x,f(x,a,b),color='red' , markersize=0.5,label=f'A={a},B={b}')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('F(X)=x^b+a^b/x^b')
  plt.grid()
  a,b=2,1
  plt.plot(x,f(x,a,b),color='blue' , markersize=0.5,label=f'A={a},B={b}')
  a,b=1,2
  plt.plot(x,f(x,a,b),color='green' ,markersize=0.5,label=f'A={a},B={b}')
  plt.legend()

  x = np.linspace(0, 0.5, 1000)
  plt.axes([0.3,0.5,0.25,0.25])
  a,b=1,1
  plt.plot(x,f(x,a,b),color='red' , markersize=0.5,label=f'A={a},B={b}')
  a,b=2,1
  plt.plot(x,f(x,a,b),color='blue' , markersize=0.5,label=f'A={a},B={b}')
  a,b=1,2
  plt.plot(x,f(x,a,b),color='green' ,markersize=0.5,label=f'A={a},B={b}')
  plt.title('for small x')
  x = np.linspace(15, 20, 1000)
  plt.axes([0.65,0.3,0.2,0.2])
  a,b=1,1
  plt.plot(x,f(x,a,b),color='red' , markersize=0.5,label=f'A={a},B={b}')
  a,b=2,1
  plt.plot(x,f(x,a,b),color='blue' , markersize=0.5,label=f'A={a},B={b}')
  a,b=1,2
  plt.plot(x,f(x,a,b),color='green' ,markersize=0.5,label=f'A={a},B={b}')
  plt.title('for big x')
gr2()
plt.show()
def gr3():
  x = np.linspace(-5, 0, 1000)
  a,b=1,1
  plt.plot(x,f(x,a,b),color='red' , markersize=0.5,label=f'A={a},B={b}')
  plt.xlabel('X')
  plt.ylabel('Y')
  plt.title('F(X)=x^b+a^b/x^b')
  plt.grid()
  a,b=2,1
  plt.plot(x,f(x,a,b),color='blue' , markersize=0.5,label=f'A={a},B={b}')
  a,b=1,2
  plt.plot(x,f(x,a,b),color='green' ,markersize=0.5,label=f'A={a},B={b}')
  y=[0]*len(x)
  plt.plot(x,y,color='black',label='y=0')
  plt.legend()
  x = np.linspace(-3, -1, 1000)
  plt.axes([0.2,0.15,0.25,0.25])
  a,b=1,1
  plt.plot(x,f(x,a,b),color='red' , markersize=0.5,label=f'A={a},B={b}')
  a,b=2,1
  plt.plot(x,f(x,a,b),color='blue' , markersize=0.5,label=f'A={a},B={b}')
  a,b=1,2
  plt.plot(x,f(x,a,b),color='green' ,markersize=0.5,label=f'A={a},B={b}')
  plt.plot(x,y,color='black',label='y=0')
  plt.title('for small x')
  
gr3()
plt.show()
def gr4():
  x = np.linspace(-2, 2, 1000)
  a,b=1,0.5
  plt.plot(x,f(x,a,b),color='red' , markersize=0.5,label=f'A={a},B={b}')
  plt.xlabel('Ось X')
  plt.ylabel('Ось Y')
  plt.title('F(X)=x^b+a^b/x^b')
  plt.grid()
  a,b=1,-0.5
  plt.plot(x,f(x,a,b),color='blue' , markersize=0.5,label=f'A={a},B={b}')
  a,b=1,-1.5
  plt.plot(x,f(x,a,b),color='green' ,markersize=0.5,label=f'A={a},B={b}')
  plt.legend()
  plt.show()
gr4()
plt.show()

def gr4_2(ax,x,a,b1,b2,mb,z,hide_labels=False):
  ax.plot(x,f(x,a,b1),label=f'a={a},b={b1}',color='red')
  ax.plot(x,f(x,a,b2),label=f'a={a},b={b1}',color='blue')
  ax.plot(x,f(x,a,mb[z][0]),label=f'a={a},b={mb[z][0]}',color='g')
  ax.plot(x,f(x,a,mb[z][1]),label=f'a={a},b={mb[z][1]}',color='m')
  ax.legend()
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_title('F(X)=x^b+a^b/x^b')
  ax.grid(True)

  ax.locator_params(nbins=3)
fig,axes=plt.subplots(1,3,figsize=(15,6))
x = np.linspace(-1, 2, 1000)
a=1
b1=0
b2=-1
mb=[[0.5,0.8],[-0.5,-0.8],[-1.5,-2.5]]
z=0

for i,ax in enumerate(axes):
  plt.ylabel('das')
  gr4_2(ax,x,a,b1,b2,mb,z)
  z+=1

plt.show()

