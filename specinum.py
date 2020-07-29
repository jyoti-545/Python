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
    print('It is special number')

else:
    print('It is not special number')

    
#without using importing math 



n = int(input('Enter the number : '))
s = 0
z = n
for i in range(len(str(n))):
    a = n%10
    b = 1
    for i in range(a,0,-1):
        b *= i
      
    s += b
    n = n//10

if s == z:
    print('It is a special number ')
else:
    print('It is not a special number')





