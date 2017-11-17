# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys

for line in sys.stdin:
    a, b, radix = map(int, line.split())
    sum_num = a + b
    rlt = []
    while(int(sum_num/radix)!=0):
        rlt.append(str(sum_num%radix))
        sum_num = int(sum_num / radix)

    rlt.append(str(sum_num%radix))
    rlt = rlt[::-1]
    print(''.join(rlt))

'''
123 456 8
'''