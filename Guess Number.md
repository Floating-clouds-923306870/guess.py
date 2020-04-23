# guess.py
#一个猜数游戏
c=1
while c==1:
    
    import random
    i=0
    x=0
    w=0
    目标=int(random.randint(0,10))
    #目标=3
    #游戏修改
    print("\n从[0,10]猜猜我是谁\n只能猜三次\n不是数字会报错的  ")

    def 测试(a):
        if int(a) in range(0,11) :
            return 0
        else:
            return 5

    while i<3 and x==0  :
        选数=int(input("试试吧\n> "))
        x=测试(选数)
        i+=1
        if x==0 and 选数==目标 :
            print(f"很好,就是{目标}\n你只用了{i}次 ")
            i=10

    if i==3 and x==0 and 选数!=目标 :
        print(f"\n你没机会了\n其实是{目标} ")    
    elif x==5 :
        w=input("\n要遵守规则\n你没机会了\n按1看结果\n>  ")    
    elif 选数==目标 and i==3:
        print(f"\n很好,就是{目标}\n你只用了{i}次 ")
        i=10 


    if  w==str(1):
        print(f"\n其实是{目标}")
    elif w!=0 and w!=str(1):
        print("？？？\n爱看不看")
    c=int(input("\n按1再来一遍\n按0退出\n>"))
