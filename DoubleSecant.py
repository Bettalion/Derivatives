from matplotlib import pyplot as plt
# Variable visualisation of derivatives
# # Things that can be changed:
# The span of x START->END ([ELENGTH,SLENGTH])
# The difference in x when doing
#   the gradient of the secant (DELTA)
# The function that is done to x (fx)line 22
# The derivative should be changed to match 
#   the derivative of function supplied (dx)line 38

# You can also use the main function to repeat for
#    different values of delta, span of x and an option of 
#    0, prints nothing to the console
#    1, prints the inaccuracies between secant and derivative
#    2, prints the inaccuracies between secant and derivative 
#       and logs them to a file

LENGTH=[0,10]
DELTA=0.1

def function(x):
 fx=(x**2)-x-4
 return fx
def truncation(value,SigFig=4):
 value=str(value)
 if len(value)>SigFig:
  value=value[:SigFig]
 return value
def main(DELTA,LENGTH,ShowTheData=1):
 SLENGTH,ELENGTH=LENGTH 
 xaxis=[]
 xsaxis=[]
 func=[]
 derivative=[]
 secant=[]

 for x in range(SLENGTH,ELENGTH):
  fx=function(x)
  dx=2*x-1
  
  xaxis.append(x)
  func.append(fx)
  derivative.append(dx)
  try:
    rise=function(x+DELTA)-function(x)
    run=DELTA
    sx1=rise/run
    rise=function(x-DELTA)-function(x)
    run=x
    sx2=rise/run
    xsaxis.append(x+DELTA)
    secant.append(sx1)
    # xsaxis.append(x-DELTA)
    # secant.append(sx2)
  except:
    pass

 diff=[]
 sum=0
 for dx,sx in zip(derivative,secant):
  inaccuracy=dx-sx
  sum+=inaccuracy
  diff.append(inaccuracy)

 plt.plot(xaxis,func)
 plt.plot(xaxis,derivative)
 plt.plot(xsaxis,secant)

 plt.show()
 if ShowTheData>=1:
  
  avgdiff=truncation(sum/len(diff))
  
  funct=[]
  derivativet=[]
  secantt=[]
  difft=[]
  
  if ShowTheData>1:
    try:
      file=open('DerivativeData.txt','a')
    except:
      file=open('DerivativeData.txt','w')
    file.write('\n\n\nData:\nFor Delta:{} and Span of x:{}'.format(DELTA,LENGTH))
    for data in [[func,funct,'Function'],[derivative,derivativet,'Derivative'],[secant,secantt,'Secant'],[diff,difft,'Inacuracy']]:
      file.write('\n{} values:\n'.format(data[2]))
      # print(data[2],len(data[0]))
      for value in data[0]:
        value=truncation(value)
        data[1].append(value)
        file.write(value)
        file.write(', ')
  else:
    for data in [[func,funct],[derivative,derivativet],[secant,secantt],[diff,difft]]:
     for value in data[0]:
      value=truncation(value)
      data[1].append(value)

  print('The inaccuracy in this example for delta:{} on avg is:{}'.format(DELTA,avgdiff))
  print('Data:\nFunction:{}\nDerivative:{}\nSecant:{}\nInacuracies:{}'.format(funct,derivativet,secantt,difft))
  
main(0.1,[-10,10],0)