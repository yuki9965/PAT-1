# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import  sys

numbers = [[], [], [], [], []]
count = 0
for line in sys.stdin:
    for n in map(int, line.split()):
        if count == 0:
            count += 1
            continue
        if n%5 in [2,3,4]:
            numbers[n%5].append(n)
        elif n%5 == 1:
            numbers[n%5].append((-1)**(len(numbers[n%5]))*n)
        else:
            numbers[n%5].append(n if n%2 == 0 else 0)

    rlt = []
    for i in range(len(numbers)):
        if len(numbers[i]) == 0:
            rlt.append('N')
            continue
        if i in [0, 1]:
            rlt.append(str(sum(numbers[i])))
        elif i == 2:
            rlt.append(str(len(numbers[i])))
        elif i == 3:
            rlt.append(str (round( sum(numbers[i])*1.0/len(numbers[i]), 1) ) )
        else:
            rlt.append(str(max(numbers[i])))
    count = 0

    print(' '.join(rlt))

#13 1 2 3 4 5 6 7 8 9 10 20 16 18