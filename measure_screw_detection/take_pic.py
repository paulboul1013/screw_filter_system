import cv2

# 创建一个摄像头对象
cap = cv2.VideoCapture(0)

save_pic_path="save.jpg"

# 检查摄像头是否成功打开
if not cap.isOpened():
    print("Could not open camera")
    exit()

# 捕获图像
ret, frame = cap.read()

# 检查图像是否成功捕获
if not ret:
    print("Could not capture image")
    exit()

# 将图像保存到文件中
cv2.imwrite(save_pic_path, frame)

# 释放摄像头对象
cap.release()

# 关闭所有打开的窗口
cv2.destroyAllWindows()
