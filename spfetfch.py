
import mysql.connector as ms

db = ms.connect(host='localhost', user='root', passwd='geetu', database='school')
cur = db.cursor()

cur.execute("select * from student")

x = cur.fetchall()

for i in x:
    print(i)
