#!/user/bin/env python3
#-*- coding: utf-8 -*-
import random
secret=random.randint(1,16)
temp=input ("猜猜我心里的数字吧，1-16之间哦:")
guess=int(temp)
while guess!=secret:
    if guess>secret:
        temp=input ("这个数字猜大了！再猜猜我心里的数字吧:")
        guess=int(temp)
    else:
        if guess==secret:
            print ("哈哈")
        else:
            temp=input ("这个数字猜小了！再猜猜我心里的数字吧:")
            guess=int(temp)
print ("猜对了！游戏结束了！")
input(r"press 'enter' to end the program")
