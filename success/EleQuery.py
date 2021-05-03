import requests
import cv2
import numpy as np
import json

class EleQuery:
  __uriCode = 'http://cwsf.whut.edu.cn/authImage'
  __uriLogin = 'http://cwsf.whut.edu.cn/innerUserLogin?logintype=PLATFORM&nickName={}&password={}&checkCode={}'
  __uriEleFee = 'http://cwsf.whut.edu.cn/querySydl?roomno={}&factorycode={}&area={}'
  __cookie = ''
  __charSet = ''

  def __init__(self):
    with open('./discern.json','r') as f:
      self.__charSet = json.loads(f.read())

  def __getCode(self):
    resp = requests.get(self.__uriCode)
    self.__cookie = '='.join(resp.cookies.items()[0])
    codeImg = cv2.imdecode(np.frombuffer(resp.content, np.uint8), 1)
    return codeImg

  def __login(self, nickName, password, checkCode):
    uri = self.__uriLogin.format(nickName, password, checkCode)
    requests.get(uri,headers={'Cookie': self.__cookie})

  def __ImageDistinguish(self, codeImg):
    im_gray = cv2.cvtColor(codeImg, cv2.COLOR_BGR2GRAY)
    ret, im_inv = cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY_INV)
    cutImage = []
    num = []
    cutImage.append(im_inv[3:15, 8:17])
    cutImage.append(im_inv[3:15, 23:32])
    cutImage.append(im_inv[3:15, 38:47])
    cutImage.append(im_inv[3:15, 53:62])
    num.append(self.__charDistinguish(cutImage[0]))
    num.append(self.__charDistinguish(cutImage[1]))
    num.append(self.__charDistinguish(cutImage[2]))
    num.append(self.__charDistinguish(cutImage[3]))
    if num.count(-1) > 0:
      checkCode = -1
    else:
      checkCode = ''.join(num)
    return checkCode

  def __charDistinguish(self, numImg):
    ks = self.__charSet.keys()
    for k in ks:
      # cnt 9 * 12 = 108
      cnt = 0 
      for i in range(12):
        for j in range(9):
          if(numImg[i][j] > 200 and self.__charSet[k][i][j] == 1):
            cnt += 1
          elif(numImg[i][j] <= 200 and self.__charSet[k][i][j] == 0):
            cnt += 1
      if(cnt > 95):
        return k
    return -1

  def __getEleFee(self, roomno, factorycode, area):
    uri = self.__uriEleFee.format(roomno, factorycode, area)
    resp = requests.get(uri, headers={'Cookie': self.__cookie})
    return resp.text

  def Get(self, nickName, password, roomno, factorycode, area):
    for i in range(10):
      codeImg = self.__getCode()
      checkCode = self.__ImageDistinguish(codeImg)
      if checkCode != -1:
        break
    if checkCode == -1:
      return -1
    self.__login(nickName, password, checkCode)
    return self.__getEleFee(roomno, factorycode, area)