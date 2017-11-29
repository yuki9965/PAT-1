# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

cur, all = 0, 0
k = 0
first_addr = ''
data_dic = {}
next_dic = {}
for line in sys.stdin:
    if cur == 0:
        first_addr, all, k = line.split()
    else:
        addr, data, next_addr = line.split()
        data_dic[addr] = data
        next_dic[addr] = next_addr


    if cur == int(all):
        cur = 0
        # print(data_dic, next_dic)
        rlt = []
        while(first_addr != '-1'):
            rlt.append(first_addr)
            first_addr = next_dic[first_addr]

        # print(rlt)
        times = int(len(rlt)/int(k))
        for i in range(times):
            rlt = rlt[:int(k)*i] + rlt[int(k)*i:int(k)*(i+1)][::-1] + rlt[int(k)*(i+1):]

        for i in range(len(rlt)):
            addr = rlt[i]
            if i != len(rlt)-1:
                print('%s %s %s' %(addr, data_dic[addr], rlt[i+1]))
            else:
                print('%s %s %s' % (addr, data_dic[addr], -1))
    cur += 1

'''
00100 6 4
00000 4 99999
00100 1 12309
68237 6 -1
33218 3 00000
99999 5 68237
12309 2 33218
'''
'''
Not all nodes are valid.
'''
