import requests
from io import BytesIO
import cv2
import numpy as np

def getImage():
  resp = requests.get('http://cwsf.whut.edu.cn/authImage')
  # for k, v in resp.cookies.items():
  #   print(k + "=" + v)
  cookie = '='.join(resp.cookies.items()[0])
  img = cv2.imdecode(np.frombuffer(resp.content, np.uint8), 1)
  cv2.imwrite('./a.jpg', img)
  return cookie, img

def ImageDistinguish(img):
  im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  ret, im_inv = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)
  cutImage1 = im_inv[3:15, 8:17]
  cutImage2 = im_inv[3:15, 23:32]
  cutImage3 = im_inv[3:15, 38:47]
  cutImage4 = im_inv[3:15, 53:62]
  cv2.waitKey(0)

def charDistinguish(img):
  return

cookie, img = getImage()
print(cookie)
ImageDistinguish(img)