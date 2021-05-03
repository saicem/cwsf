import requests
from fake_useragent import UserAgent
import cv2
import matplotlib.pyplot as plt
import numpy as np

uri_authImage = 'http://cwsf.whut.edu.cn/authImage'
uri_login = 'http://cwsf.whut.edu.cn/innerUserLogin'
uri_sydl = 'http://cwsf.whut.edu.cn/querySydl'

login_parms = {
  'logintype': 'PLATFORM',
  'nickName': '0121904950722',
  'password': '021539',
  'checkCode': '1865'
}

sydl_parms = {
  'roomno': '7795',
  'factorycode': 'E023',
  'area': '9001'
}

def save_img(img):
  img = open('img.png','wb')
  img.write(img)
  img.close()

def num_get(im_inv):
  cutImage1 = im_inv[3:15, 8:17]
  cutImage2 = im_inv[3:15, 23:32]
  cutImage3 = im_inv[3:15, 38:47]
  cutImage4 = im_inv[3:15, 53:62]
  cv2.imshow('num',cutImage1)
  cv2.imshow('num',cutImage2)
  cv2.imshow('num',cutImage3)
  cv2.imshow('num',cutImage4)

resp = requests.get(uri_authImage)
img = cv2.imdecode(np.fromstring(resp.content, np.uint8), 1)
im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, im_inv = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)
num_get(im_inv)
cv2.waitKey(0)

# requests.get(uri_login, params=login_parms)
# requests.get(uri_sydl, params=sydl_parms)