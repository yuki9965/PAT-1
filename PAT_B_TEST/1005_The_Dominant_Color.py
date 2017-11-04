# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys

cur, all = 0, 0
colors = {}

for line in sys.stdin:
    if cur == 0:
        all = int(line.split()[0])
        cur += 1
        continue
    else:
        for n in line.split():
            if n in colors.keys():
                colors[n] += 1
            else:
                colors[n] = 1

    if cur == all:
        rlt = sorted(zip(colors.values(), colors.keys()), reverse=True)
        print(rlt[0][1])
        cur = 0
        continue
    cur += 1

'''
5 3
0 0 255 16777215 24
24 24 0 0 24
24 0 24 24 24
'''