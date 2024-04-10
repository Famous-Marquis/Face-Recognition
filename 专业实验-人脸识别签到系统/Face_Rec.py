import face_recognition
import cv2

# 加载图片并识别人脸
image_path = "专业实验-人脸识别签到系统\photo\证件照19岁.jpg"  # 请替换为你的图片路径
image = face_recognition.load_image_file(image_path)
face_locations = face_recognition.face_locations(image)

# 将图片从BGR格式转换为RGB格式
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# 在图片上绘制人脸边框
for (top, right, bottom, left) in face_locations:
    cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

# 显示结果图片
cv2.imshow("Face Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

