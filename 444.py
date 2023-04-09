import cv2
import numpy as np

# 读入图片
img = cv2.imread(r'C:\\Users\\fdh32\\Pictures\\red-grey-red.png')
# 将图片转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 对图片进行滤波处理，平滑噪声
blur = cv2.medianBlur(gray, 5)

# 对图片进行二值化处理
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# 使用 Canny 边缘检测算法检测血清分层的边缘
edges = cv2.Canny(thresh, 50, 150, apertureSize=3)

# 使用霍夫直线变换检测直线段
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=100, maxLineGap=10)

# 在原图上绘制直线段
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 0), thickness=2)

# 显示结果
cv2.imshow('blood sample', img)
cv2.waitKey(0)
cv2.destroyAllWindows()