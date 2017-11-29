# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys

dic = {x:str(x) for x in range(13)}
dic[10], dic[11], dic[12] = 'A', 'B', 'C'
# print(dic)

def convert(nums):
    rlt = []
    for n in nums:
        rlt.append(dic[int(n/13)])
        rlt.append(dic[n%13])
    return rlt

for line in sys.stdin:
    nums = list(map(int, line.split()))
    rlt = convert(nums)
    print('#', end='')
    print(''.join(rlt))



'''
15 43 71
'''