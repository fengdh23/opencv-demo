import cv2
img = cv2.imread('./suoerwei2.jpeg')
print(img.shape)
img = cv2.resize(img,dsize = (1063,552))
gray = cv2.cvtColor(img, code=cv2.COLOR_BGR2GRAY)
face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
# minNeighbors 参数越大，条件越苛刻，参数越小，宽松！
# scaleFactor 参数越大，缩放越大，遗漏人脸，参数越小，细腻，找到人脸。
# faces = face_detector.detectMultiScale2(gray,
#                                         scaleFactor=1.05,
#                                         minNeighbors=3,
#                                         minSize=(25,25),
#                                         maxSize=(50,50))
faces = face_detector.detectMultiScale(gray,
                               scaleFactor=1.05,
                               minNeighbors=3,
                               minSize=(25,25),
                               maxSize=(50,50))
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,pt1=(x,y),pt2=(x+w,y + h),color=[0,0,255],thickness=2)
cv2.imshow('faces',img)
cv2.waitKey(0)
cv2.destroyAllWindows()