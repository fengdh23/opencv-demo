import cv2

import numpy as np

img = np.zeros((480, 640, 3), np.uint8)

cv2.split(img)
