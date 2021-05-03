import sys
from saicem import elequery

fileName, nickName, password, roomno, factorycode, area = sys.argv

query = elequery.EleQuery()
res = query.Get(nickName, password, roomno, factorycode, area)
if(res == 0):
  print(0)
else:
  print(str(1)+res)
# {"roomlist":{"resultInfo":{"result":"1","timeStamp":"2021-05-03T16:14:35.9129277+08:00","msg":"成功"},"remainPower":"161.55","remainName":"电量","ZVlaue":"9976.06","readTime":"2021/5/3 16:04:20"},"returncode":"SUCCESS","returnmsg":"ok"}