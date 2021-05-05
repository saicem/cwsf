from spider import EleSpider

nickName = "0121904950722"
password = "021539"
roomno = ""
factorycode = ""
area = ""
spider = EleSpider(nickName, password)
spider.getFloors()