import cv2
import numpy as np

if __name__ == '__main__':
    # split
    img = np.zeros((200, 200, 3), np.uint8)

    # 分割 : 通道 b g  r
    b, g, r = cv2.split(img)
    # 修改颜色
    b[10:100, 10:100] = 255  # white
    g[10:100, 10:100] = 255  # white
    # r[10:100, 10:100] = 255 # white

    img2 = cv2.merge((b, g, r))

    cv2.imshow('Blue', b)
    cv2.imshow('Green', g)
    cv2.imshow('Red', r)

    cv2.imshow('img', np.hstack((b, g)))
    cv2.imshow('img2', np.hstack((img, img2)))


    cv2.waitKey(0)
    cv2.destroyAllWindows()
