from matplotlib import pyplot as plt

xaxis=[]
func=[]
derivative=[]
secant=[]

LENGTH=10
DELTA=0.1

def function(x):
 fx=(x**2)-x
 return fx

for x in range(LENGTH):
 fx=function(x)
 dx=2*x-1
 
 rise=function(x+DELTA)-function(x)
 run=DELTA
 sx=rise/run
 xaxis.append(x)
 func.append(fx)
 derivative.append(dx)
 secant.append(sx)

diff=[]
sum=0
for dx,sx in zip(derivative,secant):
 inaccuracy=dx-sx
 sum+=inaccuracy
 diff.append(inaccuracy)

plt.plot(xaxis,func,)
plt.plot(xaxis,derivative)
plt.plot(xaxis,secant)

plt.show()
avgdiff=sum/len(diff)
print('The inaccuracy in this example for delta:{} on avg is:{}'.format(DELTA,avgdiff))