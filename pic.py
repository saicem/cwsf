import cv2
import numpy as np
# import tensorflow as tf
import os
# 左闭右闭 上下左右各去了一个边框
# row 2-13
# column 7-15 22-30 37-45 52-60
# 所以

pathGray = './Image_gray/'
pathPng = './Image_png/'
pathChar = './Chars/'

def GetGray():
  lsFile = os.listdir(pathPng)
  for file in lsFile:
    filename = file.split('.')[0]
    im = cv2.imread(pathPng + file)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, im_inv = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)
    cv2.imwrite(pathGray + filename + '.jpg', im_inv)

def GetChars():
  lsFile = os.listdir(pathPng)
  for file in lsFile:  
    im = cv2.imread(pathPng + file)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, im_inv = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)

    cutImage = im_inv[3:15, 8:17]
    cv2.imwrite(pathChar + file.split('.')[0] + '_1.jpg', cutImage)

    cutImage = im_inv[3:15, 23:32]
    cv2.imwrite(pathChar + file.split('.')[0] + '_2.jpg', cutImage)
    cutImage = im_inv[3:15, 38:47]
    cv2.imwrite(pathChar + file.split('.')[0] + '_3.jpg', cutImage)

    cutImage = im_inv[3:15, 53:62]
    cv2.imwrite(pathChar + file.split('.')[0] + '_4.jpg', cutImage)

# GetChars()
lsFile = os.listdir(pathChar)
img = cv2.imread(pathChar + lsFile[0], 0)
print(img)