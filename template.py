import cv2
import numpy as np
import time
import os

filepath = ''
# 读取图片
im = cv2.imread(filepath)
# img = cv2.imdecode(np.fromstring(res.content, np.uint8),1) 从网络读取
# 灰度化
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# 二值化
ret, im_inv = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)
# 降噪 模糊化
kernel = 1/16*np.array([[1,2,1], [2,4,2], [1,2,1]])
im_blur = cv2.filter2D(im_inv,-1,kernel)
# 二值化
ret, im_res = cv2.threshold(im_blur,127,255,cv2.THRESH_BINARY)
# 切割图片
im2, contours, hierarchy = cv2.findContours(im_res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = []
contour = contours[0]
x, y, w, h = cv2.boundingRect(contour)
box0 = np.int0([[x,y], [x+w/4,y], [x+w/4,y+h], [x,y+h]])
box1 = np.int0([[x+w/4,y], [x+w*2/4,y], [x+w*2/4,y+h], [x+w/4,y+h]])
box2 = np.int0([[x+w*2/4,y], [x+w*3/4,y], [x+w*3/4,y+h], [x+w*2/4,y+h]])
box3 = np.int0([[x+w*3/4,y], [x+w,y], [x+w,y+h], [x+w*3/4,y+h]])
result.extend([box0, box1, box2, box3])
# 保存图片
for box in result:
  cv2.drawContours(im, [box], 0, (0,0,255),2)
  roi = im_res[box[0][1]:box[3][1], box[0][0]:box[1][0]]
  roistd = cv2.resize(roi, (30, 30)) # 将字符图片统一调整为30x30的图片大小
  timestamp = int(time.time() * 1e6) # 为防止文件重名，使用时间戳命名文件名
  filename = "{}.jpg".format(timestamp)
  filepath = os.path.join("char", filename)
  cv2.imwrite(filepath, roistd)