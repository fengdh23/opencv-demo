import cv2
import numpy as np
img = cv2.imread('./bai.jpeg')

face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
faces = face_detector.detectMultiScale(gray)

for x,y,w,h in faces:
    # 图片：高度、宽度、像素
    face = img[y:y+h,x:x+w] # x 横坐标，宽度；y 纵坐标，高度
    face = face[::10,::10] # 信息缺失的人脸，模糊人脸
    # # face = cv2.resize(face,dsize = (w,h))
    # face = np.repeat(face,10,axis = 0)
    # face = np.repeat(face, 10, axis=1)
    # img[y:y+h,x:x+w] = face[:h,:w] # 10个中取一个像素，信息变少了
    h2,w2 = face.shape[:2]
    for i in range(h2):
        for j in range(w2):
            # 切片
            # i = 0 y:y+10
            # i = 1 y+10:y+20
            img[i*10+y:(i+1)*10+y,j*10+x:(j+1)*10+x] = face[i,j] # 一个像素抵十个像素进行替换

cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()