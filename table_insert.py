import pymysql as mq
mycon=mq.connect(host="localhost", user="root", password="", database="school")

mycur=mycon.cursor()
ins="insert into student (st_name,st_class,st_email) values (%s,%s,%s)"
val=("Abhi",'12th','abhi@gmail.com')

mycur.execute(ins,val)
mycon.commit()  

print(mycur.rowcount," was inserted")

