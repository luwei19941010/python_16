#-*-coding:utf-8-*-
# Author:Lu Wei

"""
功能：
	1.用户注册，提示用户输入用户名和密码，然后获取当前注册时间，最后将用户名、密码、注册时间写入到文件。
	2.用户登录，只有三次错误机会，一旦错误则冻结账户（下次启动也无法登录，提示：用户已经冻结）。
"""
import hashlib,json
from datetime import datetime

def md5(psd):
    obj = hashlib.md5('qazwsx'.encode('utf-8'))
    obj.update(psd.encode('utf-8'))
    psd_s = obj.hexdigest()
    return psd_s

def check_user(user):
    with open('regist.txt', mode='r', encoding='utf-8') as fr:
        flag=False
        for i in fr:
            # d=eval(i)
            d = json.loads(i.strip().replace('\'', '\"'))
            if user == d.get('username'):
                print("用户名以存在，重新输入")
                flag=True
                break
        return flag

def regist():
    with open('regist.txt',mode='a',encoding='utf-8') as fw:
        while True:
            d={}
            user = input('username:')
            if user.upper()=='N':
                return
            if check_user(user):
                continue
            psd = input('password:')
            psd_s=md5(psd)
            re_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            d['username']=user
            d['password']=psd_s
            d['time']=re_time
            fw.write(str(d)+'\n')
            fw.flush()

def login():
    while True:
        count=0
        flag=True
        l = []
        with open('regist.txt', mode='r', encoding='utf-8') as fr:
            user = input('username:')
            if user.upper() == 'N':
                return
            psd=input('password:')
            psd_s=md5(psd)
            for i in fr:
                #d=eval(i)
                d = json.loads(i.strip().replace('\'', '\"'))
                if user==d.get('username') and psd_s==d.get('password'):
                    flag=True
                else:
                    flag=False
            if flag:
                print('login ok')
                return
            else:
                print('login erros again')


while True:
    d={'1':regist,'2':login}
    print('Choice One'.center(20,'*'))
    print("""
    1.regist
    2.login
    """)
    user_choice=input('choice one：')
    if user_choice.upper()=='N':
        break
    try:
        func=d.get(user_choice)
        func()
    except Exception as e:
        print('input erros')
print('login out')

