# Guessing game
import random

C = ['Red','Blue','Yellow','Green','Orange','Pink','Brown','Black','White','Purple','Indigo']
n = input('Enter your name : ')

print('Hi',n,'\nWelcome to this Game\nThis is guessing game. You have to choose a colour from given list. If your guessing matches with computer guessing you won.\nYou have only nine chances')
print()
input('Press enter to start the game')
print()
print('List fo flowers is given below')
print(C)
print()
for i in range(9):
    a = input('Enter the name of the colour : ')
    if a == random.choice(C):
        print('----------------You Won---------------- \n---------------Game Over---------------')
        break
    elif i==8:
        print('You Lose!')
    else:
        print('You guessed wrong.\nTry Again')
        print('You have',9-i-1,'chances left')
    print()
    

input()
