import sqlite3

conn = sqlite3.connect('student_info.db')

   
conn.execute('''CREATE TABLE IF NOT EXISTS students
                (name TEXT, student_id INTEGER, class_id INTEGER, face_encoding TEXT)''')

   

conn.execute("INSERT INTO students (name, student_id, class_id) VALUES ('张三', 123456, 10)")

conn.commit()

cursor = conn.execute("SELECT * from students")
for row in cursor:
    print(row)
    #查看数据库中的数据

conn.execute("INSERT INTO students (name, student_id) VALUES ('李四', 234567)")
conn.commit()  
#插入数据
cursor = conn.execute("SELECT * from students")
for row in cursor:
    print(row)

conn.execute("UPDATE students SET name = '李四' WHERE student_id = 123456")
conn.commit()
#编辑数据
conn.execute("DELETE FROM students WHERE student_id = 123456")
conn.commit()
#删除数据

conn.execute("ALTER TABLE students ADD COLUMN email TEXT")
conn.commit()
#增添列
conn.close()
