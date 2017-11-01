# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

cur = 0
numerator, denominator = 0, 0

def gdc(a, b):
    a, b = abs(a), abs(b)
    n1 = a if a>b else b
    n2 = a + b - n1
    while(n2!=0):
        c = n1%n2
        n1 = n2
        n2 = c
    return n1

for line in sys.stdin:
    if cur == 0:
        cur += 1
        continue
    else:
        nums = line.split()
        # print(nums)
        for i in range(len(nums)):
            tmp_numerator, tmp_denominator = map(int, nums[i].split('/'))
            # print(tmp_numerator, tmp_denominator)
            if i == 0:
                numerator, denominator = tmp_numerator, tmp_denominator
            else:
                gdc_num = gdc(tmp_denominator, denominator)
                lcm_num = tmp_denominator * denominator / gdc_num
                numerator = lcm_num/denominator*numerator +lcm_num/tmp_denominator*tmp_numerator
                denominator = lcm_num
        if numerator == 0:
            print(0)
        else:
            if numerator % denominator == 0:
                print(int(numerator/denominator))
            else:
                rlt_gdc_num = gdc(denominator, numerator)
                int_part = int(numerator/denominator)
                if int_part != 0:
                    print(int_part, '%d/%d' % (int((numerator-int_part*denominator)/rlt_gdc_num), int(denominator/rlt_gdc_num)))
                else:
                    print('%d/%d' % (int(numerator/rlt_gdc_num), int(denominator/rlt_gdc_num)))
        cur += 1
    if cur == 2:
        cur = 0





'''
5
2/5 4/15 1/30 -2/60 8/3

2
-2/3 1/3

4
-1/2 -1/2 -1/2 -1/2
'''