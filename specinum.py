# to check that entered number is a special number or not

from math import *

x = int(input('Enter a number : '))
b = str(x)
s = 0
for i in range(len(b)):
    
    a = x%10
    s += factorial(a)
    x = x//10
    

if s == float(b):
    print(b,'is special number')

else:
    print(b,'is not special number')




