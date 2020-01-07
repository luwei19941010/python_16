#-*-coding:utf-8-*-
# Author:Lu Wei

with open('5.txt',mode='r',encoding='utf-8') as f:
    num = int(input('num:'))
    l = []
    for i in f:
        l.append(i.strip())
    page, a = divmod(len(l), num)
    if a > 0:
        page += 1
    while True:
        user_page=int(input('1=<LOOK_PAGE<=%s:'%page))
        start_page=num*(user_page-1)+1
        end_page=num*user_page
        # print(start_page,end_page)
        # print(l)
        flag=True
        while flag:
            print(l[0])
            for i in l[start_page:end_page+1]:
                print(i)
                if l.index(i)==end_page-1:
                    flag=False
