import sys
from EleQuery import EleQuery

fileName, nickName, password, roomno, factorycode, area = sys.argv
# nickName = '0121904950722'
# password = '021539'
# roomno = '7796'
# factorycode = 'E023'
# area = '9001'

res = EleQuery().Get(nickName, password, roomno, factorycode, area)
print(res) 
# {"roomlist":
# {"resultInfo":{"result":"1","timeStamp":"2021-05-03T18:30:41.2149563+08:00","msg":"成功"},
# "remainPower":"161.48",
# "remainName":"电量",
# "ZVlaue":"9976.13",
# "readTime":"2021/5/3 18:04:21"},
# "returncode":"SUCCESS","returnmsg":"ok"}