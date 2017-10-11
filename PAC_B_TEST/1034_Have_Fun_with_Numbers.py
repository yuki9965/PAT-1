# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

for line in sys.stdin:
    origin_num = int(line.split()[0])
    origin_cmp = line.split()[0]
    origin_cmp = list(map(int, origin_cmp))
    double_num = origin_num*2
    double_cmp = list(map(int, str(double_num)))
    origin_cmp = sorted(origin_cmp)
    double_cmp = sorted(double_cmp)
    # print (origin_cmp)
    # print (double_cmp)
    # print (double_cmp == origin_cmp)
    print("Yes") if double_cmp == origin_cmp else print("No")
    print(double_num)
'''
1234567899
'''