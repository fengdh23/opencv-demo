import cv2
import numpy as np
# 一秒多少帧，24帧
v = cv2.VideoCapture('./ttnk.mp4')
# cv2.VideoWriter()
fps = v.get(propId=cv2.CAP_PROP_FPS) #frame(帧) per second
print(fps)
w_ = v.get(propId=cv2.CAP_PROP_FRAME_WIDTH)
h_ = v.get(propId=cv2.CAP_PROP_FRAME_HEIGHT)
print(int(w_//2),int(h_//2))
face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
while True: # 死循环
    flag,frame = v.read()
    # 最后一张图片后面，没有图片了，无法读取图片，返回False
    if flag == False:
        break # 退出
    frame = cv2.resize(frame,dsize=(int(w_//2),int(h_//2)))
    gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
    # 播放慢了，检测人脸耗时操作，扫描整张图片，图片大，耗时长
    # faces = face_detector.detectMultiScale(gray)
    # for x,y,w,h in faces:
    #     cv2.rectangle(frame,pt1 = (x,y),pt2 = (x+w,y+h),color=[0,0,255],thickness=2)
    cv2.imshow('frame',gray)
    key = cv2.waitKey(10) # 等待键盘输入的Key 键盘
    if key == ord('q'):
        break
cv2.destroyAllWindows()
v.release() # 释放，视频流