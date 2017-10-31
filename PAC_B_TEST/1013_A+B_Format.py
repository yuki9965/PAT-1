# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys

for line in sys.stdin:
    a, b = map(int, line.strip().split())
    rlt = a + b
    length = len(str(rlt)) if rlt >= 0 else len(str(rlt)) - 1
    rlt = str(rlt)
    rlt = rlt[::-1]
    if length%3 == 0:
        n = int(length/3) - 1
    else:
        n = int(length/3)
    i = 1
    while(n>0):
        rlt = rlt[:i*4-1] + ',' + rlt[i*4-1:]
        i += 1
        n -= 1

    rlt = rlt[::-1]
    print(rlt)


'''
-1000000 9
'''