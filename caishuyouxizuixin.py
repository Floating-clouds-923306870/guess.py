import os
import json

a=(open("用户.py")).read()
a=a.replace("\'","\"")
m=json.loads(a)


def 注册():
    nnn=1
    global 用户名
    while nnn==1:
        用户名=input("请输入用户名\n> ")
        if 用户名 in a:
            print("这个被用过了\n换个用户名吧")
        else :
            密码=input(f"{用户名} 的密码\n> ")
            m[用户名]=密码
            aa=open("用户.py","w")
            aa.write(str(m))
            aa.close()
            print("注册成功")
            nnn=2
    os.mknod(f"{用户名}.py")
    op=open(f"{用户名}.py","w")
    op.write("1000");op.close()
    i=input("直接登陆 >1\n退出 >2\n> ")
    if i==str(1):
        i==0
    elif i==str(2):
        exit(0) 
    else:
        exit("滚吧")  

def 登陆():
    global 用户名
    用户名=input("用户名是\n> ")
    密码=m.get(用户名)
    if not 用户名:
        print("没有用户\n请注册")
        注册()
    else:
        nn=1
        while nn==1:
            密码吗=input(f"欢迎回来{用户名}\n密码是> ")
            if 密码吗==密码:
                nn=11
            else:
                print("错了 再试试吧")
            

import random
def 准备():
    print("从1到1000猜一个数\n先试一个吧")
    global 目标
    目标 =random.randint (1,1001)
    #目标=100
    #游戏修改

def 检验(a):
    if a>目标:
        print ("再小点")
        return 0
    elif a<目标:
        print ("再大点")
        return 0
    else:
        print(f"没错 就是{目标}")
        return 1
def 游戏():
    i=0
    global n
    n=0
    while i==0:
        选数=int(input("> "))
        i=检验(选数)
        n+=1

def 记录一():
    w=open("游戏记录录.py")
    ww=w.read()
    r=ww.split("\n") 
    w.close()   
    w=open("游戏记录录.py","a")
    w.write( "\n"+str(n))
    w.close()

    z=0
    for j in r:
        if n>=int(j):
            z+=1
        else:
            www=1
    ss=1000           
    for j in r:
         if int(j)<ss:
             ss=int(j)
         else:
             www=1
    if z==0:
        print(f"新纪录！你只用了{n}次")
    else:
        print(f"你没有超越其他玩家\n最高纪录{ss}次")

def 记录二():
    w=open(f"{用户名}.py")
    ww=w.read()
    r=ww.split("\n") 
    w.close()   
    w=open(f"{用户名}.py","a")
    w.write( "\n"+str(n))
    w.close()

    z=0
    for j in r:
        if n>=int(j):
            z+=1
        else:
            www=1
    ss=1000           
    for j in r:
         if int(j)<ss:
             ss=int(j)
         else:
             www=1
    if z==0:
        print(f"新纪录！你只用了{n}次")
    else:
        print(f"你没有超越其他玩家\n最高纪录{ss}次")

def 对战结果():
    if n%2 ==1:
        print(f"{先手}胜")
    else:
        print(f"{后手}胜")
    


n=555
nn=input("快速模式 >1\n个人模式 >2\n对战模式 >3\n> ")

if nn==str(1): 
    准备()
    游戏()
    记录一()      
elif nn==str(2) :
    while n==555:
        n=input("登陆输入 1\n注册输入 2\n> ")
        if n==str(2):
            注册()
        elif n==str(1):
            登陆()
        else:
            print("你在逗我")
            n=555
    print("登陆成功")
    准备()
    游戏()
    记录二()   
else:
    先手=input("先手是\n> ")
    后手=input("后手是\n> ")
    准备()
    游戏()
    对战结果()
