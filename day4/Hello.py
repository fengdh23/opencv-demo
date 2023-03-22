import numpy as np
# a = [[1,2],[3,4],[-2,-7],[2,8]]
# a = np.asarray(a)
# # 索引
# print(a[0,0],a[0,1])
# # 遍历 二维数组中的数据[1,2]，两个数，分别使用x，y接收
# for x,y in a:# 遍历，两层，所以遍历第一层
#     print('--------------',x,y)
# nd = np.random.randint(0,10,size = (4,5))
# print(nd)
#
# nd2 = np.repeat(nd, 5, axis=1)
# print(nd2)

# nd = np.array([255,255,255])
# cond = nd == 255
# print(cond)
# print(cond.all())

# a = 97 A = 65
# print(ord('A'))
# print(ord('q'))
# print(ord('中'))
# print('MP4V')
# l = [*'MPVV']
# print(l)
# print(*'MP4V')
a = np.array([1,2,3,5])
print(a)
print(a.reshape([4,1,1]))