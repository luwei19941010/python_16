#-*-coding:utf-8-*-
# Author:Lu Wei
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

