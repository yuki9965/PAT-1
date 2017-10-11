# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

cur, all = 0,0

ids = {}
grades = {}

for line in sys.stdin:
    if cur == 0:
        all = int(line)
        cur += 1
        continue
    elif cur == all+1:
        cur = 0
        flag = 0
        down, up = map(int, line.split())
        for n in sorted(zip(grades.values(), grades.keys()), reverse=True):
            if down <= n[0] <= up:
                print(n[1], ids[n[1]])
                flag = 1
        if flag == 0:
            print("NONE")
    else:
        name, id, grade = map(str, line.split())
        ids[name] = id
        grades[name] = int(grade)


    cur += 1
'''
4
Tom CS000001 59
Joe Math990112 89
Mike CS991301 100
Mary EE990830 95
60 100
'''