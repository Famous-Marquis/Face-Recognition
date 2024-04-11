import cv2
import dlib
import numpy as np
import sqlite3
import pickle
       


# 加载预训练的人脸检测器和关键点预测器
face_detector = cv2.CascadeClassifier('opencv\\data\\haarcascades\\haarcascade_frontalface_default.xml')
landmark_predictor = dlib.shape_predictor('SHIT\\shape_predictor_68_face_landmarks.dat')

# 从摄像头获取视频流
cap = cv2.VideoCapture(0)

while True:
    # 读取一帧图像
    ret, frame = cap.read()
    if not ret:
        break

    # 将图像转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用人脸检测器检测人脸
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # 在原图像上绘制人脸矩形框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 提取人脸区域
        face_roi = gray[y:y+h, x:x+w]

        # 使用关键点预测器提取人脸特征点
        landmarks = landmark_predictor(face_roi, dlib.rectangle(0, 0, w, h))

        # 遍历并标记关键点
        for i in range(68):
            x = landmarks.part(i).x + x
            y = landmarks.part(i).y + y
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)


# 连接到SQLite数据库
    conn = sqlite3.connect('SHIT\\face_info.db')
    c = conn.cursor()
    # 遍历所有人脸的特征值，并与扫描出的特征值进行相似度计算

    for (x, y, w, h) in faces:
        # 提取人脸区域
        face_roi = gray[y:y+h, x:x+w]

        # 使用关键点预测器提取人脸特征点
        landmarks = landmark_predictor(face_roi, dlib.rectangle(0, 0, w, h))

        
        # 遍历并标记关键点
        landmarks_np = np.zeros((68, 2), dtype=int)

        
        for i in range(68):
            landmarks_np[i] = (landmarks.part(i).x, landmarks.part(i).y)


 #逐个读取不同学生的face_features
        print("逐个读取不同学生的face_features")
        conn = sqlite3.connect("SHIT\\face_info.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM face_info")
        rows = cursor.fetchall()
        for row in rows:
            face_features = pickle.loads(row[3])
        # 计算当前帧与数据库中所有人脸特征的相似度
            # 实际的方法可能需要根据你的数据结构进行调整
            landmarks_np_array = np.array([[point.x, point.y] for point in landmarks.parts()])
            face_features_array = np.array([[point.x, point.y] for point in face_features.parts()])
            # 现在你可以使用转换后的数组进行矩阵乘法运算
            similarity = np.dot(face_features_array, np.transpose(landmarks_np_array)) / (np.linalg.norm(face_features_array) * np.linalg.norm(landmarks_np_array))

    if similarity > 0.5:
        # 找到相似度最高的学生
        print("找到相似度最高的学生")
        name = row[1]
        print(name)
        break
    else:
        print("没有找到相似度最高的学生")
        


    

          
    cv2.imshow('Face Detection', frame)
    # 关闭数据库连接
    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()