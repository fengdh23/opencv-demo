import cv2

# 读取输入图像
img = cv2.imread('full_red.png')

# 获取图像的宽度和高度
height, width = img.shape[:2]
print('height', height)
print('height', width)
# 计算裁剪区域的左上角坐标和右下角坐标
x1 = int(width / 2 - 20)
x2 = int(width / 2 + 20)
y1 = 0
y2 = height

# 使用cv2.crop函数进行裁剪
cropped = img[y1:y2, x1:x2]
cropped_img = img[y1:y2, x1:x2].copy()  # .copy() ??
# 显示输出图像
# cv2.imshow('output', cropped)
cv2.imshow('output2', cropped_img)
cv2.waitKey()