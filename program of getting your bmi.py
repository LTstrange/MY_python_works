#!/user/bin/env python3
#-*- coding: utf-8 -*-

print("Enter your height and weight, I'll tell your \"bmi\"")
height = float(input('How tall are you (m):'))
weight = float(input('How weight are you (kg):'))
bmi = weight / (height*height)
if bmi <18.5:
    print('过轻')
elif bmi <25:
    print('正常')
elif bmi <28:
    print('过重')
elif bmi <32:
    print('肥胖')
else:
    print('严重肥胖')
input(r'press "enter" to end the program')
