import random

total = int(input("total="))#录入单个随机数集合的总数
cycle = int(input("cycle="))#录入模拟模型循环次数
accuracy = float(input("accuracy="))#注意在输入时请输入 除一百可整的数字,即"(100/accuracy)= int" 以防出错

ratelist = []#ratelist中收录了当前rate值下的numberlist中的平均值
rate = 0
while rate < 100:
    #循环程序开始
    numberlist = []   #数组列表
    cycleA = 0
    while cycleA < cycle:
        #创建随机数列
        member = []
        i = 0
        while i < total:
            temp = random.randint(0,100)
            member.append(temp)
            i += 1
        #截取前比率最大值
        temp2 = len(member) * (rate / 100)
        x = int (temp + 0.5)
        MAX = 0
        for somenum in member[0:x]:
            if MAX <= somenum:
                MAX = somenum
        #print ("程序进行中：",(int((cycleA / cycle)*1000))/10,"%")   #这里是最耗时的部分，没有这条，程序用时为现在的近十分之一
        answer = False  #这个位置的语句：1不能没有 2不能是true 3无论这里是什么，都只对total很小的时候起作用 求大神解答
        for a in member[x:len(member)]:    #选取后比率大于MAX的第一个数值
            if a >= MAX:
                del member
                answer = True
                break
            else:
                answer = False
        if answer ==True:
            numberlist.append(a)
        cycleA += 1

    #找出numberlist中的平均值
    tote = 0
    for digit in numberlist:
        tote += digit
    if len(numberlist) != 0:
        ratelist.append(int((tote / len(numberlist))+0.5))
    else:
        ratelist.append(0)
    rate += accuracy
    print(rate)

for z,b in enumerate(ratelist):
    if b == max(ratelist):
        print("最大比率为：",(z/(100/accuracy))*100,"%")
