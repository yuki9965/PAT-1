# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys
cur, all = 0, 0
rlt = {}

for line in sys.stdin:
    if cur == 0:
        all = int(line)
        cur += 1
        continue
    else:
        a, b = map(int, line.split())
        if a in rlt:
            rlt[a] += b
        else:
            rlt[a] = b


    if cur == all:
        break

    cur += 1


n = max(zip(rlt.values(), rlt.keys()))
print(n[1], n[0])

'''
6
3 65
2 80
1 100
2 70
3 40
3 0
'''