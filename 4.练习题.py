#-*-coding:utf-8-*-
# Author:Lu Wei

# #压缩文件src
# #压缩文件到code
# #将文件解压到D:\x1目录中
# import shutil,datetime,os
# ctime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
# if not os.path.exists('code'):
#     os.makedirs('code')
# shutil.make_archive(os.path.join('code',ctime),'zip',r'C:\Users\davidlu\PycharmProjects\luwei-Knightsplan\day16\src')
# dst_file=os.path.join('code',ctime)+'.zip'
# shutil.unpack_archive(dst_file,r'D:\x1','zip')

#############################################
import requests

def func(arg):
    l = []

    for i in arg:
        try:
            response = requests.get(i)
            l.append(response.text)
        except Exception as e:
            pass
        return l
