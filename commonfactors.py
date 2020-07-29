# to find the common factors of two numbers

x = int(input('Enter the first number : '))
y = int(input('Enter the second number : '))
l = [x]
m = [y]

def fac(a,b):
    for i in range(1,(a//2)+1):
        if a % i == 0:
            b.append(i)
        else:
            pass
    b.sort()
    return b

f1 = fac(x,l)
f2 = fac(y,m)

if len(f1)>=len(f2):
    z = len(f1)
else:
    z = len(f2)


c = []
def com():
    for i in f1:
        for j in f2:
            if i == j:
                c.append(i)
            else:
                pass
    return c

result = com()
print('Common factors of',x,y,'are',result)
