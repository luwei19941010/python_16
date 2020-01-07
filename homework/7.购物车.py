#-*-coding:utf-8-*-
# Author:Lu Wei
# 购物车
import os
from datetime import datetime
date=datetime.now().strftime('%Y_%m_%d')
with open(date+'.txt',mode='a',encoding='utf-8') as fa,open(date+'.txt',mode='r',encoding='utf-8') as fr:
    SHOPPING_CAR = {}
    l=[]
    # 商品列表
    GOODS_LIST = [
        {'id':1,'title':'飞机','price':1000},
        {'id':3,'title':'大炮','price':1000},
        {'id':8,'title':'迫击炮','price':1000},
        {'id':9,'title':'手枪','price':1000},
    ]
    for i in GOODS_LIST:
        print(i)
    user_choice=int(input('选择商品ID:'))
    user_num=int(input('选择商品数量:'))
    for i in fr:
        i=eval(i.strip())
        l.append(i)


    if len(l)!=0:
        for i in l:
            if i['id']==user_choice:
                i['num']=i['num']+user_num
            else:
                for i in GOODS_LIST:
                    if i['id']==user_choice:
                        SHOPPING_CAR.update(i)
                        SHOPPING_CAR['num']=user_num
                        l.append(SHOPPING_CAR)
    else:
        for i in GOODS_LIST:
            if i['id'] == user_choice:
                SHOPPING_CAR.update(i)
                SHOPPING_CAR['num'] = user_num
                l.append(SHOPPING_CAR)

with open(date+'.txt',mode='w',encoding='utf-8') as fw:
    for i in l:
        fw.write(str(i) + '\n')
