import face_recognition
import cv2
import pickle

# 加载本地存储的人脸特征值
with open("face_encodings.pkl", "rb") as f:
    stored_face_encodings = pickle.load(f)

# 打开摄像头
video_capture = cv2.VideoCapture(0)

while True:
    # 从摄像头捕获一帧画面
    ret, frame = video_capture.read()

    # 将画面转换为RGB格式
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 在画面中识别人脸
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # 遍历识别到的人脸
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # 遍历本地存储的人脸特征值进行比对
        matches = face_recognition.compare_faces(stored_face_encodings, face_encoding)

        if True in matches:
            # 如果匹配成功，显示人脸信息
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, "Matched", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
        else:
            # 如果匹配失败，显示未知
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, "Unknown", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # 显示结果画面
    cv2.imshow("Face Recognition", frame)

    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 释放资源并关闭窗口
video_capture.release()
cv2.destroyAllWindows()