import face_recognition
import pickle

# 加载本地存储的照片
image_path = "专业实验-人脸识别签到系统\photo\证件照19岁.jpg"  # 请替换为你的图片路径
image = face_recognition.load_image_file(image_path)

# 分析照片中的人脸特征值
face_encodings = face_recognition.face_encodings(image)

# 将特征值存储在文件中
with open("face_encodings.pkl", "wb") as f:
    pickle.dump(face_encodings, f)