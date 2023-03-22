import numpy as np
import  cv2
xi = cv2.imread('../xi.jpeg')
print(xi.shape)
rose = cv2.imread('../rose2.jpg')
print(rose.shape)
rose = cv2.resize(rose,(480,600)) # 尺寸调整，宽度、高度
print(rose.shape)
xi = cv2.addWeighted(xi,0.7,rose,0.3,gamma=1.0)
cv2.imshow('xi',xi)
cv2.waitKey(0)
cv2.destroyAllWindows()
