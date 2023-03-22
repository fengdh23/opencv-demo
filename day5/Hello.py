# l = list('abcdefjhi')
#
# for i,j in enumerate(l,10):
#     print(i,j)
from skimage import io,data,exposure # scikit-image过程中
import matplotlib.pyplot as plt # pip install matplotlib
import cv2
moon = data.moon()
print(moon.shape)
moon2 = cv2.equalizeHist(moon)
moon3 = exposure.equalize_hist(moon) # 曝光
# plt.imshow(moon,cmap='gray')
# plt.show()

cv2.imshow('moon',moon)
cv2.waitKey(0)
#
cv2.imshow('moon',moon3)
cv2.waitKey(0)
cv2.destroyAllWindows()