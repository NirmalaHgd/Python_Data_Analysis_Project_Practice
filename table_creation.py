import pymysql as mq
mycon=mq.connect(host="localhost",user="root",password="",database="school")
print(mycon)


mycur=mycon.cursor()
cr="create table Student (st_id INT primary key auto_increment, st_name VARCHAR(50), st_class VARCHAR(10), st_email VARCHAR(50))"
mycur.execute(cr)
