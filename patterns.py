#printing patterns

for k in range(6):    
    for i in range(7):
        for j in range(6-i):
            print(' ',end='')
        for j in range(i*2+1):
            print('*',end='')
        print(' ',end='')
        for l in range(4):
            for j in range(6-i):
                print(' '*2,end='')
            for j in range(i*2+1):
                print('*',end='')
            print(' ',end='') 
        
        print()
    for i in range(7):
        for j in range(1,i+1):
            print(' ',end='')
        for j in range((7-i)*2-1):
            print('*',end='')
        print(' ',end='')
        for l in range(4):
            for j in range(1,i+1):
                print(' '*2, end ='')
            for j in range((7-i)*2-1):
                print('*',end='')
            print(' ',end='')
        
        print()
    
    
