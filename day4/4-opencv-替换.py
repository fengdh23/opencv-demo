import cv2
import numpy as np
img = cv2.imread('./bai.jpeg')
face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
faces = face_detector.detectMultiScale(gray)
star = cv2.imread('./star.jpg')
print(star)
for x,y,w,h in faces:
    # 把五角星，放到额头正中间
    star2 = cv2.resize(star, dsize=(w//6, h//6))
    # img[y:y+h//6,x + 5*w//12: 5*w//12+x+w//6] = star2
    for i in range(h//6):
        for j in range(w//6):
            if (star2[i,j] > 200).all():# 大白色
                pass # 不赋值
            else: # 不是大白色，赋值
                img[i + y,j + x + 5*w//12]=star2[i,j]

cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()