import cv2


cv2.namedWindow('video',cv2.WINDOW_NORMAL)

cv2.resizeWindow('video',640,480)
# 第一个设备 索引, 不同的设备可能会不一样 1 2
# 异常 cv::obsensor::getStreamChannelGroup Camera index out of range
cap = cv2.VideoCapture(0)

while cap.isOpened():
# 循环读取摄像头的每一帧
# while True:
    # 读一帧数据，返回标识和这一帧的数据，True 标识读到了数据
    ret, frame = cap.read()
    if not ret:
        # 没读到数据,直接退出
        break
    cv2.imshow('video', frame)

    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()

# 打开视频
# cv2.VideoCapture('./xxx.mp4')

# *mp4v 就是解包操作，等同于 ‘m’，‘p’，‘4’，‘v’
# cv2.VideoWriter_fourcc(*'mp4v')