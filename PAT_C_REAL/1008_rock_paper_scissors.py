# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys

rlt_signal_player1 = {'B': 0, 'C': 0, 'J': 0}
rlt_signal_player2 = {'B': 0, 'C': 0, 'J': 0}
rlt_win_player1 = [0, 0, 0]


def r_p_s_calculate(a, b):
    # print(a, b)
    if ord(a) - ord(b) == 0:
        return ([0, 1, 0], 0)
    elif ord(a) - ord(b) in [-7, -1, 8]:
        return ([1, 0, 0], 1)
    elif ord(a) - ord(b) in [7, 1, -8]:
        return ([0, 0, 1], -1)


# print(ord('C'), ord('J'), ord('B'),[x+y for x,y in zip([1,0,1],[1,0,1])])
# print(' '.join(map(str,rlt_win_player1)))
current = 0
num = 0
for line in sys.stdin:

    if current == 0:
        # print(n)
        n = line.split()
        num = int(n[0])
        current += 1
        continue
    else:
        a, b = line.split()
        (rlt_temp, rlt_flag) = r_p_s_calculate(a, b)
        if rlt_flag == 1:
            rlt_signal_player1[a] += 1
        elif rlt_flag == -1:
            rlt_signal_player2[b] += 1
        rlt_win_player1 = [x + y for x, y in zip(rlt_win_player1, rlt_temp)]
        # print(current, num)


    if current == num:
        print(' '.join(map(str, rlt_win_player1)))
        print(' '.join(map(str, rlt_win_player1[::-1])))
        print(max(rlt_signal_player1.items(), key=lambda x: x[1])[0], max(rlt_signal_player2.items(), key=lambda x: x[1])[0])

    current += 1
'''
10  
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J
'''