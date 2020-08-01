

# to create a menu driven program

print('Hey there,')
print('Here are some operations you can do')

print('''Enter
"oddeven"    (To check whether a number is odd or even) 
"sumeven"    (To find the sum of even numbers)
"sumodd"     (To find the sum of odd numbers) 
"exit"       (To find exit the program)

''')



def oddeven():
    x = int(input('Enter the number : '))
    if x % 2 == 0:
        print('It is even number.')
    else:
        print('It is odd number')

def sumeven():
    s = 0
    a = int(input('Enter the lower limit : '))
    b = int(input('Enter the upper limit : '))
    if b%2 ==0:
        for i in range(a,b+1):
            if i %2 == 0:
                s +=i
            else:
                pass
    else:
        for i in range(a,b):
            if i % 2== 0:
                s +=i
    return s

                
def sumodd():
    s = 0
    a = int(input('Enter the lower limit : '))
    b = int(input('Enter the upper limit : '))
    if b % 2 != 0:
        for i in range(a,b+1):
            if i%2!=0:
                s +=i
            else:
                pass
    else:
        for i in range(a,b):
            if i%2 != 0:
                s +=i
            else:
                pass
    return s
    

for i in range(9):
    x = input('Enter the operation you want to do : ')
    if x == 'oddeven':
        oddeven()

    elif x == 'sumeven':
        result = sumeven()
        print('Sum of even numbers =',result)

    elif x == 'sumodd':
        result = sumodd()
        print('Sum of odd numbers =',result)

    elif x == 'exit':
        quit()

    else:
        print('"Sorry, this operation is not available" or "You may have enter the wrong value"')

    input()










            
