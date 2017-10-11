# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

wight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
Z = {'0':'1', '1':'0', '2':'X', '3':'9', '4':'8', '5':'7', '6':'6', '7':'5', '8':'4', '9':'3', '10':'2'}
cur, all = 0, 0
rlt = []

for line in sys.stdin:
    if cur == 0:
        all = int(line)
        cur += 1
        continue
    else:
        sumNum = 0
        idcard = line.split()[0]
        # print(idcard)
        for n in range(len(idcard)-1):
            if idcard[n].isalpha() == True:
                rlt.append(''.join(idcard))
                sumNum = -1
                break
            else:
                sumNum += int(idcard[n]) * wight[n]
        if(sumNum != -1 and Z[str(int(sumNum%11))] != idcard[17]):
            rlt.append(''.join(idcard))

    if cur == all:
        break
    cur += 1

if len(rlt):
    print('\n'.join(rlt))
else:
    print("All passed")

'''
4
320124198808240056
12010X198901011234
110108196711301866
37070419881216001X
'''