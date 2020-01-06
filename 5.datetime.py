#-*-coding:utf-8-*-
# Author:Lu Wei
import time
from datetime import datetime,timezone,timedelta
'''
v1=datetime.now()#当前本地时间
print(v1)
v2=datetime.utcnow()#当前UTC时间
print(v2)
tz=timezone(timedelta(hours=7))#指定时区时间
v3=datetime.now(tz)
print(v3)


##########datetime格式转str#######
v4=v1.strftime('%Y/%m/%d %H:%M:%S')
print(v4)
print(type(v4))

##########str格式转datetime#######
v5='2011-11-11'
v6=datetime.strptime(v5,'%Y-%m-%d')
v7=v6-timedelta(days=10)
v8=v7.strftime('%Y-%m-%d')
print(v6,type(v6))
print(v7,type(v7))
print(v8,type(v8))



########时间戳和datetme关系#########
ctime=time.time()
print(ctime)
v1=datetime.fromtimestamp(ctime)
print(v1)
dz=datetime.now()
cz=dz.timestamp()
print(cz)
'''
v=datetime.now()
# 1.datetime转str
s=v.strftime('%Y-%m-%d %H:%M:%S')
print(s,type(s))
# 2.str转datetime
d=datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
print(d,type(d))
# 3.datetime转timestamp
t=datetime.timestamp(v)
print(t,type(t))
# 4.timestamp转datetime
d1=datetime.fromtimestamp(t)
print(d1,type(d1))
#时间加减
#datetime=datetime-timedelta(hours=)
#a=time.strftime("%Y-%m-%d")
a=time.strptime("2017-03-16","%Y-%m-%d")
print(a)