import cv2
import numpy as np

# 读入图片
img = cv2.imread(r'C:\\Users\\fdh32\\Pictures\\red-blue2.jpg')

# 将图片转换为 HSV 颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 设置红色和蓝色的阈值范围
lower_red = np.array([0, 50, 50])
upper_red = np.array([10, 255, 255])
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# 分割红色和蓝色区域
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

# 检测红色区域的直线
edges_red = cv2.Canny(mask_red, 50, 150, apertureSize=3)
lines_red = cv2.HoughLines(edges_red, 1, np.pi / 180, 200)

# 检测蓝色区域的直线
edges_blue = cv2.Canny(mask_blue, 50, 150, apertureSize=3)
lines_blue = cv2.HoughLines(edges_blue, 1, np.pi / 180, 200)

# 绘制红色区域的直线
for line in lines_red:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

# 绘制蓝色区域的直线
for line in lines_blue:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

# 显示结果
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()