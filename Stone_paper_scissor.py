import random

print("----------------------HI----------------------")
print("-------------WELCOME TO OUR GAME--------------")

print("              STONE PAPER SCISSOR             ")
name = str(input("Please enter your name : "))
print("---------------Hello",name+"----------------")


print("-----------------Game Info------------------")
print("You have to type what you choose stone, paper or scissor")
print()
print("Letter case doesn't matter")
print()

print("--------Are you ready for the game----------")
input("press enter  to start   : ")

l = ('stone', 'paper', 'scissor')
while True:
    c = str(input("Enter what you choose  :   "))  
    c = c.lower()
    a = random.randrange(len(l))
    a = l[a]
    print(a)
    if a == c :
        print('-----------Match Draw-----------')
    elif a == 'stone' and c == 'paper' :
        print('------------You Won------------')
    elif a == 'paper' and c == 'scissor':
        print('------------You Won------------')
    elif a == 'scissor' and c == 'stone':
        print('------------You Won-------------')        
    else:
        print('-----Better Luck Next Time-----\n')        
    x = input("Press y you want to continue and any other key if you want to exit  : ")

    if x == 'y':
        continue
    else:
        print("-----------Thank you for playing --------------")
        print("----------Hope your enjoyed the Game ----------")
        break
