import sqlite3

conn = sqlite3.connect('student_info.db')

   
conn.execute('''CREATE TABLE IF NOT EXISTS students
                (name TEXT, student_id INTEGER, attendance INTEGER)''')

   

conn.execute("INSERT INTO students (name, student_id, attendance) VALUES ('张三', 123456, 10)")

conn.commit()

cursor = conn.execute("SELECT * from students")
for row in cursor:
    print(row)
    #查看数据库中的数据

conn.execute("INSERT INTO students (name, student_id, attendance) VALUES ('李四', 234567, 5)")
conn.commit()  
#插入数据
cursor = conn.execute("SELECT * from students")
for row in cursor:
    print(row)

conn.execute("DELETE FROM students WHERE student_id = 123456")
conn.commit()
#删除数据

conn.execute("ALTER TABLE students ADD COLUMN email TEXT")
conn.commit()
#增添列
conn.close()
## 创建一个空字典
#face_recognition_info = {}

# 添加学号和对应的人脸信息
#face_recognition_info['123456'] = '人脸信息1'
#face_recognition_info['234567'] = '人脸信息2'
#face_recognition_info['345678'] = '人脸信息3'