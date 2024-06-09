import pymysql as mq

mycon=mq.connect(host="localhost", user="root",password="")
print(mycon)

mycur=mycon.cursor()
try:
    db="create database school"
    mycur.execute(db)
    print("Database created")

except:
    print("Database error")