# finding the mean, median and mode of numbers in a list entered by user by defining a function

n = int(input('Enter the total no. of frequecies : '))
l = []

for i in range(1,n+1):
    x = int(input('Enter the number : '))
    l.append(x)
l.sort()
print(l)

def mean():
    Mean =sum(l)/n
    return round(Mean,2)
    
def median():
    if n%2 ==0:
        a = n//2
        b = a-1
        Median =l[b],',',l[a]
        return Median
    else:
        a = (n+1)//2
        Median =l[a-1]
        return Median

def mode():
    a = max(set(l), key = l.count)
    Mode = a
    return Mode

print('Mean =',mean())
print('Median =',median())
print('Mode =',mode())
