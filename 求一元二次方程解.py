#!/user/bin/env python3
#-*- coding: utf-8 -*-

import math
def quadratic(a,b,c):
    ans1 = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    ans2 = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
    return ans1,ans2
print('输入二次方程的abc值，返回两个解')
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if (b*b - 4*a*c) >= 0:
    answer = quadratic(a,b,c)
    print(answer)
else:
    print('no answer')


