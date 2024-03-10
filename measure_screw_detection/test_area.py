import cv2
import numpy as np

# 创建一张黑色背景图像
img = np.zeros((500, 500, 3), dtype=np.uint8)

# 定义两个点作为直线的起点和终点
start_point = (50, 50)
end_point = (450, 50)

# 定义线条的颜色和厚度
line_color = (0, 255, 0) # 绿色
line_thickness = 2

# 绘制第一条线
cv2.line(img, start_point, end_point, line_color, line_thickness)

# 计算平行线的偏移量
offset = 30
delta_x, delta_y = end_point[0] - start_point[0], end_point[1] - start_point[1]
dx, dy = delta_y, -delta_x
dx_norm, dy_norm = dx / np.sqrt(dx**2 + dy**2), dy / np.sqrt(dx**2 + dy**2)
offset_x, offset_y = int(offset * dx_norm), int(offset * dy_norm)

# 计算平行线的起点和终点
start_point2 = (start_point[0] + offset_x, start_point[1] + offset_y)
end_point2 = (end_point[0] + offset_x, end_point[1] + offset_y)

# 绘制第二条线
cv2.line(img, start_point2, end_point2, line_color, line_thickness)

# 显示图像
cv2.imshow("Parallel Lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
