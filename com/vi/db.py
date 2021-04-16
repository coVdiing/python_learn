# _*_ coding:UTF-8 _*_
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
print(cursor)
# cursor.execute('CREATE TABLE student(id INT(10) PRIMARY KEY AUTO_INCREMENT,name VARCHAR(20))')
# cursor.execute("INSERT INTO student VALUES(1,'Joey')")
cursor.execute("SELECT * FROM student")
student = cursor.fetchall()
print(student)
conn.commit()
cursor.close()
conn.close()
