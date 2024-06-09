import pymysql as mq
mycon=mq.connect(host="localhost",user='root',passwd='',database='school')

mycur=mycon.cursor()
sel_q="select * from student"
mycur.execute(sel_q)
res=mycur.fetchall()
for i in res:
    print(i)