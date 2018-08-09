#!/user/bin/env python3
#-*- coding: utf-8 -*-

def R():
    n = 1
    while True:
        n = n+1
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = R() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)

print(1)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break
