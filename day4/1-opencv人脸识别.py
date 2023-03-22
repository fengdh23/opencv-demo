import numpy as np
import cv2

img = cv2.imread('./bai.jpeg')
# 人脸：眼睛、嘴巴、鼻子、额头、脸颊、眉毛……
# 人脸蒙一半，人（高级算法）识别，上面有眼睛
# 眼睛：瞳孔，瞳孔外面是白色的
# 鼻子：两个孔，形状
# 级联算法，图片中，找特征，满足一部分，特征，算做人脸
face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
print(img.shape)
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
print(gray.shape)
# 坐标，左上角坐标，宽度、高度
faces = face_detector.detectMultiScale(gray) # 检测人脸
print(faces)
for x,y,w,h in faces:
    # cv2.rectangle(img,#标记图片
    #               pt1 = (x,y),# 左上角
    #               pt2=(x+w,y+h),#右下角
    #               color=[0,0,255],#颜色
    #               thickness=2)#线宽
    cv2.circle(img,
               center=(x + w//2,y + h//2),#圆心
               radius=h//2,#半径
               color=[0,0,255],# 颜色
               thickness=2)#线宽
    cv2.putText(img = img,
                text='bai',#显示文本
                org = (x,y),#位置
                fontFace=cv2.FONT_HERSHEY_TRIPLEX,#字体
                fontScale=2,#字号
                color=[0,0,255],#颜色
                thickness=2)#线宽


cv2.imshow('face',img)
cv2.waitKey(0)
cv2.destroyAllWindows()