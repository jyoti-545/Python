
import mysql.connector as ms

db = ms.connect(host='localhost', user='root', passwd='geetu', database='school')
cur = db.cursor()


cur.execute("alter table student add column ContactNO varchar(10)")
db.commit()

cur.close()
db.close()
