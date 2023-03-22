import cv2
import numpy as np
# 一秒多少帧，24帧
v = cv2.VideoCapture('./ttnk.mp4')
fourcc = v.get(propId=cv2.CAP_PROP_FOURCC)
print(fourcc)
writer = cv2.VideoWriter(filename = './gray.mp4',fourcc = cv2.VideoWriter.fourcc(*'MP4V'),fps = 24,frameSize = (1280,720))
while True: # 死循环
    flag,frame = v.read()
    # 最后一张图片后面，没有图片了，无法读取图片，返回False
    if flag == False:
        break # 退出
    gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
    gray = np.reshape(gray,[720,1280,1]) # 增加一维
    gray = np.repeat(gray, 3, axis=-1) # 本来彩色，但是蓝绿红，一样，波动，绚丽色彩
    print('-------gray:',gray.shape)
    print('------frame:',frame.shape)
    cv2.imshow('frame',gray)
    writer.write(gray) # 存的是黑白
    key = cv2.waitKey(10) # 等待键盘输入的Key 键盘
    if key == ord('q'):
        break
cv2.destroyAllWindows()
v.release() # 释放，视频流
writer.release()