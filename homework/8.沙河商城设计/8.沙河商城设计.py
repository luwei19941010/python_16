#-*-coding:utf-8-*-
# Author:Lu Wei
"""
功能：
	1.用户注册，提示用户输入用户名和密码，然后获取当前注册时间，最后将用户名、密码、注册时间写入到文件。
	2.用户登录，只有三次错误机会，一旦错误则冻结账户（下次启动也无法登录，提示：用户已经冻结）。
	3.商品浏览，分页显示商品（小文件）； 用户可以选择商品且可以选择数量然后加入购物车（在全局变量操作），
	  不再购买之后，需要讲购物车信息写入到文件，文件要写入到指定目录：
		shopping_car(文件夹)
			- 用户名A(文件夹)
				2019-11-11-09-59.txt
				2019-11-12-11-56.txt
				2019-12-11-11-47.txt
			- 用户B(文件夹)
				2019-11-11-11-11.txt
				2019-11-12-11-15.txt
				2019-12-11-11-22.txt
	  注意：重复购买同一件商品时，只更改购物车中的数量。
	4.我的购物车，查看用户所有的购物车记录，即：找到shopping_car目录下当前用户所有的购买信息，并显示：
		2019-11-11-09-59
			飞机|1000|10个
			大炮|2000|3个
		2019-11-12-11-56.txt
			迫击炮|10000|10个
			手枪|123|3个

	5.用户未登录的情况下，如果访问 商品流程 、我的购物车 时，提示登录之后才能访问，让用户先去选择登录（装饰器实现）。
"""
import os
from datetime import datetime

def regist():
    while True:
        user_l=[]
        user_d={}
        flag=True
        r_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        username=input('please regist your username[N:exit()]:')
        if username.upper()=='N':
            return
        password=input('please regist your password:')
        with open('user_date.txt',mode='a',encoding='utf-8') as fa,open('user_date.txt',mode='r',encoding='utf-8') as fr:
            for i in fr:
                user_l.append(eval(i))
            if len(user_l)==0:
                user_d['username']=username
                user_d['password']=password
                user_d['r_time']=r_time
                user_d['lock']=True
                user_d['login']=0
                fa.write(str(user_d)+'\n')
                fa.flush()
                continue
            for i in user_l:
                if i['username']==username:
                    flag=False
            if flag:
                user_d['username']=username
                user_d['password']=password
                user_d['r_time']=r_time
                user_d['lock']=True
                user_d['login']=0
                fa.write(str(user_d)+'\n')
                fa.flush()
            else:
                print('请重新注册，用户名已注册')

def login():
    count = 0
    while True:
        user_l=[]
        flag=False
        count+=1
        user_name=input('login username:')
        if user_name.upper()=='N':
            return
        user_psd=input('login password:')
        with open('user_date.txt',mode='r',encoding='utf-8') as fr:
            for i in fr:
                user_l.append(eval(i))
            for i in user_l:
                if i['username']==user_name:
                    if not i['lock']:
                        print('无法登录，用户已经冻结')
                        return
                if i['username']==user_name and i['password']==user_psd:
                    i['login']=1
                    with open('user_date.txt', mode='w', encoding='utf-8') as fw:
                        for i in user_l:
                            fw.write(str(i)+'\n')
                    flag=True
                    break
                if count == 3:
                    print('三次输入错误')
                    i['lock']=False
                    with open('user_date.txt', mode='w', encoding='utf-8') as fw:
                        for i in user_l:
                            fw.write(str(i)+'\n')
                    return
            if flag:
                print('登录成功')
                shop(user_name)
                return
            else:
                print('登录失败')

def shopping(username):
    l=[]
    l_buy=[]
    num = int(input('每页显示几行:'))
    with open('shop_list.txt', mode='r', encoding='utf-8') as fr:
        for i in fr:
            l.append(i.strip())
    while True:
        page,a=divmod(len(l),num)
        if a>0:
            page+=1
        user_page=input('请输入页码1至%s,N exit():'%(page,))
        if user_page.upper()=='N':
            return
        start_page=num*(int(user_page)-1)+1
        end_page=num*int(user_page)
        print(l[0])
        for i in l[start_page:end_page+1]:
            print(l.index(i),i)
        id=input('请输入购买商品id,N exit():')
        if id.upper()=='N':
            continue
        num1=input('商品数量:')
      #  l_buy.append(l[int(id)] + '|%s' % (num1,))
        path1=r'shopping_car/%s'%(username)
        path2=datetime.now().strftime('%Y-%m-%d-%H-%M')
        path3=os.path.join(path1,path2)+'.txt'
        if not os.path.exists(path1):#pytharm下无需绝对路径
            os.makedirs(path1)
        with open(path3, mode='a', encoding='utf-8') as fr:
            #for i in l_buy:
            fr.write(l[int(id)] + '|%s' % (num1,)+'\n')
            fr.flush()

def shoping_car(username):
    print('购物车清单'.center(30,'*'))
    file_path = os.path.dirname(os.path.abspath(__file__))
    user_file = file_path + '\\shopping_car' + '\\%s'%(username,)
    for x, y, z in os.walk(user_file):
        for i in z:
            print(i)
            with open(os.path.join(user_file, i), mode='r', encoding='utf-8') as fr:
                for i in fr:
                    print(i.strip())

def shop(username):
    while True:
        d = {'1': shopping, '2': shoping_car}
        print('沙河商城【购物】'.center(30, '*'))
        print("""
        1.shopping
        2.shoping_car
        """)
        user_choice=input('请选择:')
        # try:
        if user_choice.upper() == 'N':
            return
        func = d.get(user_choice)
        func(username)
        # except Exception as  e:
        #     print('输入错误')

def rest():
    user_l=[]
    with open('user_date.txt', mode='r', encoding='utf-8') as fr:
        for i in fr:
            user_l.append(eval(i))
        for i in user_l:
            i['lock']=True
            i['login']=0
    with open('user_date.txt', mode='w', encoding='utf-8') as fw:
        for i in user_l:
            fw.write(str(i)+'\n')

while True:
    d={'1':regist,'2':login}
    print('沙河商城主页'.center(30,'*'))
    print("""
    1.regist
    2.login
    """)
    user_choice=input('请选择:')
    # try:
    if user_choice.upper()=='N':
        break
    func=d.get(user_choice)
    func()
    # except Exception as  e:
    #     print('输入错误')
rest()
print('欢迎使用，拜拜'.zfill(20))

