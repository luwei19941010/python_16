### day16

#### 1.今日内容

- 模块基础知识
- time/datatime
- json/picle
- shutil
- logging
- 其他

#### 2.内容回顾&补充

##### 2.1模块（类库）

- 内置模块
- 第三方模块
- 自定义模块

面试题：

- 常用内置模块有哪些？ json/time/  os/sys

##### 2.2定义模块

定义模块时可以把一个py文件或一个文件夹（包）当作一个模块，以方便于以后其他py文件的调用

对于包的定义：

py2：文件中必须有‘  _ _ init _ _.py’

py3：不需要‘  _ _ init _ _.py’，但建议还是写上。

##### 2.3模块的调用

###### 2.3.1示例一

```
XXX模块
def show():
	print('哈哈是多少')
def func():
	pass
print(456)
```

```
#导入模块，加载此模块所有的值到内存。
import XXX
print(123) 
#调用模块中的函数
XXX.func()

--->456  123

```

```
from XXX import func,show
from XXX import *
func()
show()
```

导入模块

- import 模块 模块.函数（）
- from 模块import函数 函数（） 
- from 模块import函数 as 别名



###### 2.3.2实例二

```
lizhong
	-jd.py
	-pdd.py
	-tb.py
包.py
```

```
import lizhong.jd
lizhong.jd.f1()
类似
from lizhong import jd 
jd.func
或者
from lizhong.jd import func
func()
```

总结：

- 模块和要执行的文件在同一目录，且需要模块内多个功能时，建议直接import模块 
- 其他推荐： from 模块 import 模块， 模块.函数（）
- 其他推荐：from 模块.模块 import 函数 ，函数（）
- 还存在 import 模块.模块  ， 模块.模块.函数（）

###注意以上import 模块行为就是为了 sys.path中没有以上模块目录。

![image-20200105133110222](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200105133110222.png)

![image-20200105133208799](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200105133208799.png)



跨层级import

![image-20200105164138393](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200105164138393.png)

将运行脚本的目录，加入到sys.path中

![image-20200105165454386](C:\Users\davidlu\AppData\Roaming\Typora\typora-user-images\image-20200105165454386.png)



##### 2.4内置模块

- os  

  - os.path.dirname() /上次目录
  - os.path.abspath() /绝对路径
  - os.path.jion(a,b)  /拼接
  - os.path.exists()  /是否存在
  - os.walk()
  - os.listdir()
  - os.makedirs()
  - os.mkdir()
  - os.rename()
  - os.stat().st_size

- sys

  - sys.path.append()

- time

- json

  - json内容中有中文，序列化是json.dumps（data，ensure_ascii=false）

    ```
    v={'k1':123,'name':'陆威'}
    data=json.dumps(v,ensure_ascii=False)
    print(data)
    {"name": "陆威", "k1": 123}
    ```

  - （json到python格式）loads 反序列化

  - （python格式到json）dumps 序列化

  - load

  ```
  with open('json.txt',mode='r',encoding='utf-8') as r:
      context=json.load(r)
      print(context,type(context))
  ```

  - dump 

  ```
  v={'k1':123,'name':'陆威'}
  with open('json.txt',mode='w',encoding='utf-8') as f:
      data=json.dump(v,f,ensure_ascii=False)
      print()
  ```

  

- hashlib

- random

- getpass

- shutil

- copy

#### 3.今日内容

##### 3.1.json和pickle

- json，优点所有语言通用，但是：只能序列化基本数据类型，list/dict/int/bool/str。
- pickle（序列化时 直接就是二进制），优点：python中所有的东西都可以被序列化（scoket对象）：缺点 只能在python中使用

##### 3.2.shutil模块

```
import  shutil
#删除文件夹
#shutil.rmtree('aa')

#重命名
#shutil.move('2.字节类型.py','2222')
#shutil.move('2222','2.字节类型.py')

#压缩
shutil.make_archive('zz','zip',r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day16\src')

#解压,没有目录则自动创建
shutil.unpack_archive('zz.zip',r'D:\x',format='zip')
```

练习题：

```
#压缩文件src
#压缩文件到code
#将文件解压到D:\x1目录中
import shutil,datetime,os
ctime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
if not os.path.exists('code'):
    os.makedirs('code')
shutil.make_archive(os.path.join('code',ctime),'zip',r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day16\src')
dst_file=os.path.join('code',ctime)+'.zip'
shutil.unpack_archive(dst_file,r'D:\x1','zip')
```

##### 3.3.time&datime

time模块

UTC/GMT：世界时间

本地时间：本地时区的时间

- time.time(),时间戳，1970-1-1 00：00开始计数的秒数。
- time.sleep(),等待秒数
- time.timezone

4.4.datetime模块

########datetime获取内容格式为datetime类型

```
from datetime import datetime,timezone,timedelta

v1=datetime.now()#当前本地时间
print(v1)
v2=datetime.utcnow()#当前UTC时间
print(v2)
tz=timezone(timedelta(hours=7))#指定时区时间
v3=datetime.now(tz)
print(v3)
print(type(v3))#->'<class 'datetime.datetime'>'
```

##########将datetime.datetime格式转换为str#############

```
v1=datetime.now()#当前本地时间
print(v1)
v4=v1.strftime('%Y/%m/%d %H:%M:%S')
print(v4)
print(type(v4))
```

##########将str格式转换为datetime.datetime############

```
v5='2011-11-11'
v6=datetime.strptime(v5,'%Y-%m-%d')
print(v6,type(v6))
```

格式化字符串时间：格式化的时间字符串format string

```
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
```

#时间戳与datetime关系

```
ctime=time.time()
print(ctime)
v1=datetime.fromtimestamp(ctime)#时间戳转换为时间
print(v1)
```

```
dz=datetime.now()
cz=dz.timestamp()#时间转换为时间戳
print(cz)
```

datetime总结：

```
v=datetime.now()
```

1.datetime转str

```
s=v.strftime('%Y-%m-%d %H:%M:%S')
print(s,type(s))
```

2.str转datetime

```
d=datetime.strptime(s,'%Y-%m-%d %H:%M:%S')
print(d,type(d))
```

3.datetime转timestamp

```
t=datetime.timestamp(v)
print(t,type(t))
```

4.timestamp转datetime

```
d1=datetime.fromtimestamp(t)
print(d1,type(d1))
```

5.时间相加减

```
新datetime=老datetime-timedelta(hours=)
```

##### 3.4.logging

##### 3.5.异常处理

将程序错误进行处理，使得程序错误不影响整体程序的执行

```
try:
    user=int(input('shuzi: '))
    print(user)
except Exception as e:
    print('err')
```



练习题：

```
#写函数，函数接受一个列表，请将列表中的元素每个都+100
def func(arg):
    l = []
    try:
        for i in arg:
            response = requests.get(i)
            l.append(response.text)
    except Exception as e:
        pass
        return l
     
     
 def func(arg):
    l = []
    for i in arg:
        try:
            response = requests.get(i)
            l.append(response.text)
        except Exception as e:
            pass
        return l
```

