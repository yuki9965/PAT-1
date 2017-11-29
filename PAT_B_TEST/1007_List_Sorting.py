# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys
from operator import itemgetter

class Student:
    def __init__(self, stuid, name, grade):
        self.stuid = stuid
        self.name = name
        self.grade = grade

    def __repr__(self):
        return repr((self.stuid, self.name, self.grade))

cur, all, op = 0, 0, 0
students = []

for line in sys.stdin:
    if cur == 0:
        all, op = map(int, line.split())
        cur += 1
        continue
    else:
        stuid, name, grade = line.split()
        students.append((stuid, name, grade))

    if cur == all:
        # print(students)
        students = sorted(students, key=lambda x:(x[op-1], x[0]))
        for stu in students:
            print(' '.join(stu))
        students = []
        cur = 0
        continue

    cur += 1

'''
5 3
000007 James 85
000010 Amy 90
000001 Zoe 60
000003 Zoe 70
000004 Goy 70
'''

'''
lambda x:(e1, e2)
prority e1>e2
'''
