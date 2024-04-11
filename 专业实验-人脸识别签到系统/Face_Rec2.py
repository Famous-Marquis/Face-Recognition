import cv2
import dlib
import numpy as np

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

    # 显示带有人脸检测结果的图像
    cv2.imshow('Face Detection', frame)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源并关闭窗口
cap.release()
cv2.destroyAllWindows()