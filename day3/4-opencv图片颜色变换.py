import cv2
import numpy as np
rose = cv2.imread('../rose2.jpg')
# COLOR_BGR2GRAY 颜色变化，BGR 三通道，变成灰色，即黑白
# gray = cv2.cvtColor(rose, code=cv2.COLOR_BGR2GRAY)
print(2**8)
gray = rose.mean(axis = -1).astype(np.uint8) # 无符号 数字0~255
threshod,gray = cv2.threshold(gray, 125, 255, type=cv2.THRESH_OTSU)
print(gray)
cv2.imshow('rose',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()