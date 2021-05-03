# 电费查询


## 介绍

这是一个关于电费查询的爬虫


## 必要条件

pip install opencv-python
pip install numpy
pip install fake_useragent


## 请求分析


### 获取验证码和cookie
请求 http://cwsf.whut.edu.cn/authImage 


### 登录
请求 http://cwsf.whut.edu.cn/innerUserLogin 请求表单
```
logintype=PLATFORM
nickName=学工号
password=密码
checkCode=验证码
```


### 获取数据
请求 http://cwsf.whut.edu.cn/querySydl 获取数据 请求表单
```
roomno=7796
factorycode=E023
area=9001
```


## 获取所有宿舍号


### 校区选择
请求 http://cwsf.whut.edu.cn/queryCampusList?factorycode=E023&area=9001&Area_ID=2
```
Area_ID=2&factorycode=E023&area=9001 # 马房山东院
Area_ID=3&factorycode=E023&area=9002 # 马房山西院
Area_ID=1&factorycode=E023&area=9003 # 南湖校区南院
Area_ID=3&factorycode=E023&area=9002 # 南湖校区北院
```
> 鉴湖和西院的请求表单一样，乐了。


### 还没写

# 