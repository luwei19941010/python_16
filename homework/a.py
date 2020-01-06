#-*-coding:utf-8-*-
# Author:Lu Wei
import json
with open('regist.txt', mode='a', encoding='utf-8') as fw, open('regist.txt', mode='r', encoding='utf-8') as fr:
    while True:
        #d = {}
        user = input('username:')
        for i in fr:
            # d=eval(i)
            print(i.strip(),type(i))
            d = json.loads(i.strip().replace('\'','\"'))
            print(d)