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
- time
- json
- hashlib
- random
- getpass
- shutil
- copy



















