# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import datetime

import sys

unlock_time, lock_time = datetime.datetime.strptime('23:59:59', '%H:%M:%S'), datetime.datetime.strptime('00:00:00', '%H:%M:%S')
unlock, lock = '', ''
cur, all = 0, 0

for line in sys.stdin:
    if cur == 0:
        all = int(line)
    else:
        id, start_time, end_time = line.split()
        start_time = datetime.datetime.strptime(start_time, '%H:%M:%S')
        end_time = datetime.datetime.strptime(end_time, '%H:%M:%S')
        if start_time < unlock_time:
            unlock = id
            unlock_time = start_time
        if end_time > lock_time:
            lock = id
            lock_time = end_time

    if cur == all:
        print(unlock, lock)
        cur = 0
    cur += 1

# start_time = datetime.datetime.strptime('15:30:28', '%H:%M:%S')
# end_time = datetime.datetime.strptime('17:00:10', '%H:%M:%S')
#
# print(start_time > end_time)

'''
3
CS301111 15:30:28 17:00:10
SC3021234 08:00:00 11:25:25
CS301133 21:45:00 21:58:40
'''