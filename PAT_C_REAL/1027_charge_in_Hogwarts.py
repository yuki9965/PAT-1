# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys

for line in sys.stdin:
    price, pay = line.split()
    price = list(map(int, price.split('.')))
    pay = list(map(int, pay.split('.')))
    flag = True if pay[0]*17*29+pay[1]*29+pay[2] > price[0]*17*29+price[1]*29+price[2] else False
    if flag:
        charge = [x - y for (y, x) in zip(price, pay)] #pay>price
    else:
        charge = [x - y for (x, y) in zip(price, pay)] #price>pay
    # print(price, pay)
    radix = [17, 29]
    for i in range(2, 0, -1):
        while charge[i]<0:
            charge[i-1] -= 1
            charge[i] += radix[i-1]

    charge = list(map(str, charge))
    print('.'.join(charge)) if flag else print('-'+'.'.join(charge))


'''
10.16.27 14.1.28
1000.15.13 323.15.28
'''