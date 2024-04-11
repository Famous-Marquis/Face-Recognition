import dlib
import cv2
import pickle
import os
import sqlite3
class Face_info:
    def __init__(self, face_features,name,id,class_id):
        self.face_features = [face_features]
        self.name = name
        self.id = id
        self.class_id = class_id


def extract_face_features(image_path, face_detector, landmark_predictor):
    # 读取图片
    img = cv2.imread(image_path)
    # 将图片转换为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 使用人脸检测器检测人脸
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # 遍历检测到的人脸
    for (x, y, w, h) in faces:
        # 提取人脸区域
        face = gray[y:y+h, x:x+w]
        # 使用特征点预测器提取特征点
        shape = landmark_predictor(face, dlib.rectangle(0, 0, w, h))
        # 返回特征点
        return shape

# 初始化人脸检测器和特征点预测器
face_detector = cv2.CascadeClassifier('opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml')
landmark_predictor = dlib.shape_predictor('SHIT\\shape_predictor_68_face_landmarks.dat')

# 提取本地图片的特征点
image_path = 'SHIT\photo\hjl.jpg'
face_features = extract_face_features(image_path, face_detector, landmark_predictor)
print(face_features)
    
print('请输入学号：')
id = input()
print('请输入姓名：')
name = input()
print('请输入班级：')
class_id = input()




print("仅仅人脸存储成功！")
print('输出人脸特征值：')
print(face_features)

# 将信息存储在数据库中
conn = sqlite3.connect("SHIT\\face_info.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS face_info (id INTEGER PRIMARY KEY, name TEXT, class_id TEXT, face_features BLOB)")

# 转换为二进制数据
face_features_data = pickle.dumps(face_features)

# 插入数据
cursor.execute("INSERT INTO face_info (name, class_id, face_features, id) VALUES (?,?,?,?)", (name, class_id, face_features_data, id))
conn.commit()
conn.close()

print("信息存储成功！")
#展示存储数据
conn = sqlite3.connect("SHIT\\face_info.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM face_info")
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
#从数据库中读取数据
print("从数据库中读取数据")
conn = sqlite3.connect("SHIT\\face_info.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM face_info WHERE id=?", (id,))
row = cursor.fetchone()
if row is not None:
    face_features = pickle.loads(row[3])
    print(face_features)
conn.close()

#逐个读取不同学生的face_features
print("逐个读取不同学生的face_features")
conn = sqlite3.connect("SHIT\\face_info.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM face_info")
rows = cursor.fetchall()
for row in rows:
    face_features = pickle.loads(row[3])
    print(face_features)
conn.close()

#删除数据库中的数据
print("删除数据库中的数据")
conn = sqlite3.connect("SHIT\\face_info.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM face_info WHERE id=?", (id,))
conn.commit()
conn.close()

