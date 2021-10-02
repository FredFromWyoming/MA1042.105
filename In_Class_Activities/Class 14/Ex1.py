import matplotlib.pyplot as plt
import numpy as np

start = -4
end = 4

def fx(x):          # f(x) = x^2
  return (x**2) -4

def gx (x):
  return -(x**2) + 4

x1 = range(start,end+1)
x2 = np.array(x1)

y1 = []
y2 = []

for i in x2:
  yOne = fx(i)
  yTwo = gx(i)

  if (yOne == yTwo):
    plt.scatter(i,yOne,50,"blue")

  y1.append(yOne)
  y2.append(yTwo)    

plt.plot(x1,y1)
plt.plot(x2,y2)

plt.grid(True)
plt.xticks([start,start/2,0,end/2,end]) 
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Actividad 14")

plt.show()
