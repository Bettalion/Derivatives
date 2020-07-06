from matplotlib import pyplot as plt

# # Things that can be changed:
# The span of x (LENGTH)
# The difference in x when doing
#   the gradient of the secant (DELTA)
# The function that is done to x (fx)line 12
# The derivative should be changed to match 
#   the derivative of function supplied (dx)line 28

# You can also use the main function to 

LENGTH=10
DELTA=0.1

def function(x):
 fx=(x**2)-x-4
 return fx
def truncation(value,SigFig=4):
 value=str(value)
 if len(value)>SigFig:
  value=value[:SigFig]
 return value
def main(DELTA,LENGTH,ShowTheDataAtTheEnd=True):
 xaxis=[]
 func=[]
 derivative=[]
 secant=[]

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
 if ShowTheDataAtTheEnd=True:
  
  avgdiff=truncation(sum/len(diff))
  
  funct=[]
  derivativet=[]
  secantt=[]
  difft=[]
  for data in [[func,funct],[derivative,derivativet],[secant,secantt],[diff,difft]]:
   for value in data[0]:
    value=truncation(value)
    data[1].append(value)
  print('The inaccuracy in this example for delta:{} on avg is:{}'.format(DELTA,avgdiff))
  print('Data:\nFunction:{}\nDerivative:{}\nSecant:{}\nInacuracies:{}'.format(funct,derivativet,secantt,difft))

main(DELTA,LENGTH)