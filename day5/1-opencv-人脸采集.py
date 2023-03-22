# 人脸检测，找到人脸，不关心是谁
# 人脸识别，校验，这个人脸是谁，分辨，验证
# 火车站刷脸进展：检测人脸，身份证（人脸）
# 检测到的人脸和身份证的人脸进行比对，一样，放行
# 和人工检票，类似的
# 比对，特征相似，允许存在误差
import cv2
cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
filename = 1
flag_write = False
while True:
    flag,frame = cap.read()
    if flag == False:
        break
    gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray,minNeighbors=10)
    print('----------------',faces)
    for x,y,w,h in faces:
        if flag_write:
            face = gray[y:y+h,x:x+w] # 获取人脸，保存，30张
            # 调整人脸尺寸，统一尺寸
            face = cv2.resize(face, dsize=(64, 64))
            cv2.imwrite('./lfk/%d.jpg'%(filename),face)
            filename += 1 # 自增
        cv2.rectangle(frame,pt1 = (x,y),pt2 = (x+w,y+h),
                      color = [0,0,255],thickness=2)
    if filename > 40:
        break
    cv2.imshow('face',frame)
    key = cv2.waitKey(1000 // 24)
    if key == ord('q'):
        break
    if key == ord('w'):
        flag_write = True # 表明写入数据
cv2.destroyAllWindows()
cap.release()