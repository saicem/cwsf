import requests
import cv2
import numpy as np
from saicem.imgDistinguish import charDistinguish
import time


class EleSpider:
    __uriCode = "http://cwsf.whut.edu.cn/authImage"
    __uriLogin = "http://cwsf.whut.edu.cn/innerUserLogin?logintype=PLATFORM&nickName={}&password={}&checkCode={}"
    __uriFloor = "http://cwsf.whut.edu.cn/queryFloorsList?{}"
    __uriRoom = "http://cwsf.whut.edu.cn/queryRoomList?floor={}&ArchitectureID={}&factorycode={}&area={}"
    __uriEleFee = "http://cwsf.whut.edu.cn/querySydl?roomno={}&factorycode={}&area={}"
    __cookie = ""
    __areas = [
        "Area_ID=2&factorycode=E023&area=9001",  # 马房山东院
        "Area_ID=3&factorycode=E023&area=9002",  # 马房山西院
        "Area_ID=1&factorycode=E023&area=9003",  # 南湖校区南院
        "Area_ID=3&factorycode=E023&area=9002",  # 南湖校区北院
    ]

    def __init__(self, nickName, password) -> None:
        for i in range(10):
            codeImg = self.__getCode()
            checkCode = self.__ImageDistinguish(codeImg)
            if checkCode != -1:
                break
        if checkCode == -1:
            return 0
        self.__login(nickName, password, checkCode)

    def __getCode(self):
        resp = requests.get(self.__uriCode)
        self.__cookie = "=".join(resp.cookies.items()[0])
        codeImg = cv2.imdecode(np.frombuffer(resp.content, np.uint8), 1)
        return codeImg

    def __ImageDistinguish(self, codeImg):
        im_gray = cv2.cvtColor(codeImg, cv2.COLOR_BGR2GRAY)
        ret, im_inv = cv2.threshold(im_gray, 127, 255, cv2.THRESH_BINARY_INV)
        cutImage = []
        num = []
        cutImage.append(im_inv[3:15, 8:17])
        cutImage.append(im_inv[3:15, 23:32])
        cutImage.append(im_inv[3:15, 38:47])
        cutImage.append(im_inv[3:15, 53:62])
        num.append(charDistinguish(cutImage[0]))
        num.append(charDistinguish(cutImage[1]))
        num.append(charDistinguish(cutImage[2]))
        num.append(charDistinguish(cutImage[3]))
        if num.count(-1) > 0:
            checkCode = -1
        else:
            checkCode = "".join(num)
        return checkCode

    def __login(self, nickName, password, checkCode):
        uri = self.__uriLogin.format(nickName, password, checkCode)
        requests.get(uri, headers={"Cookie": self.__cookie})

    def __webQuery(self, uri):
        return requests.get(uri,headers={"Cookie": self.__cookie})

    def getFloors(self):
        areas = self.__areas
        for area in areas:
            uri = self.__uriFloor.format(area)
            resp = self.__webQuery(uri)
            if resp.status_code != 200:
                print("something wrong in getFloors")
            return resp.text

    def getFee(self, roomno, factorycode, area):
        uri = self.__uriEleFee.format(roomno, factorycode, area)
        resp = self.__webQuery(uri)
        return resp.text

# {
#     "buildinglist": [
#         {
#             "ArchitectureID": "55",
#             "ArchitectureName": "东10舍（原东院11舍）",
#             "ArchitectureStorys": "7",
#             "ArchitectureBegin": "1",
#             "ArchitectureUnit": "楼"
#         }
#     ],
#     "returncode": "SUCCESS",
#     "returnmsg": "ok"
# }

# {
#     "roomlist": {
#         "resultInfo": {
#             "result": "1",
#             "timeStamp": "2021-05-03T16:14:35.9129277+08:00",
#             "msg": "成功",
#         },
#         "remainPower": "161.55",
#         "remainName": "电量",
#         "ZVlaue": "9976.06",
#         "readTime": "2021/5/3 16:04:20",
#     },
#     "returncode": "SUCCESS",
#     "returnmsg": "ok",
# }
