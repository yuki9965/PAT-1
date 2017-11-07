# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys

nums = {}
cur = 0
flag = False

for line in sys.stdin:
    exponents = 0
    for n in list(map(float, line.split()))[1:]:
        if flag:
            nums[exponents] = nums[exponents] + n if exponents in nums.keys() else n
            if nums[exponents] == 0:
                nums.pop(exponents)
        else:
            exponents = n

        flag = not flag

    cur += 1
    if cur == 2:
        cur = 0
        rlt = []

        rlt.append(str(len(nums)))
        for (x, y) in sorted(zip(nums.keys(), nums.values()), reverse=True):
            rlt.append(str(int(x)))
            # rlt.append(str(int(y)) if y == int(y) else str(y))
            rlt.append('{0:.1f}'.format(y))
        print(' '.join(rlt))


'''
2 1 2.4 0 3.2
2 2 1.5 1 0.5
'''

'''
3 999 5 100 -5 0 -0.5
4 100 5 10 -1 3 5.7 0 10
'''

'''
4 7 516.6 6 969.5 5 289.5 2 894.3
8 10 409.7 7 374.8 6 132.1 5 405.7 4 804.9 3 678.7 2 191.2 0 11.6
'''