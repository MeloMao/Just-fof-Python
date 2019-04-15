# -*- coding: UTF-8 -*-

import datetime
from datetime import date

y1,m1,d1 = map(int, input("请输入起始年月日，用空格符号隔开：").split())
date1 = date(y1,m1,d1)
y2,m2,d2 = map(int, input("请输入结束年月日，用空格符号隔开：").split())
date2 = date(y2,m2,d2)

date_delta = date2 - date1
date_num = str(date_delta)
if(len(date_num) == 14):
    print("日期差为"+date_num[0:1]+"天")
elif(len(date_num) == 16):
    print("日期差为"+date_num[0:2]+"天")
elif(len(date_num) == 18):
    print("日期差为"+date_num[0:4]+"天")
else:
    print("日期差为"+date_num[0:3]+"天")