#!/user/bin/env python3
# -*- coding: utf-8 -*-
s1 = int(input('之前的成绩：'))
s2 = int(input('之后的成绩：'))
r = ((s2 - s1) / s1)*100
print('%.2f%%' % r)
input(r'press "enter" to end the program')
