
# program to count number of repetition of letter

f1 = open("text.txt","w")           
    
f1.write("This is a python program. In which will count the number of repetition of letters 'A' and 'e' irrespective of case")

f1.close()

f2 = open("text.txt","r")

a = f2.read()

c1 = c2 = 0
list1 = []
list2 = []

a = a.lower()

for i in a:
    if i == 'a':
        c1 += 1
        list1.append(c1)
    elif i == 'e':
        c2 += 1
        list2.append(c2)
    else:
        pass

print("Counting list for 'a'",list1)
print("Counting list for 'e'",list2)
print()
print("Letter 'a' repeats",c1,"times in the text file")
print("Letter 'e' repeats",c2,"times in the text file")
