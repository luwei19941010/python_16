#-*-coding:utf-8-*-
# Author:Lu Wei
import os,sys,json
path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
import client
#from lib import jd
#jd.fjd1()
#from lib.jd import fjd1
#fjd1()
import lib.jd
lib.jd.fjd1()
client.fc1()

v={'k1':123,'name':'陆威'}
with open('json.txt',mode='w',encoding='utf-8') as f:
    data=json.dump(v,f,ensure_ascii=False)
    print()
with open('json.txt',mode='r',encoding='utf-8') as r:
    context=json.load(r)
    print(context,type(context))
# data=json.dumps(v,ensure_ascii=False)
# print(data)












