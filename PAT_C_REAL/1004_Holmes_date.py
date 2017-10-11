# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import sys
day = {'A':'MON', 'B':'TUE', 'C':'WED', 'D':'THU', 'E':'FRI', 'F':'SAT', 'G':'SUN'}
hour = {'0':'00', '1':'01', '2':'02', '3':'03', '4':'04', '5':'05', '6':'06', '7':'07', '8':'08', '9':'09',
        'A':'10', 'B':'11', 'C':'12', 'D':'13', 'E':'14', 'F':'15', 'G':'16', 'H':'17', 'I':'18', 'J':'19',
        'K':'20', 'L':'21', 'M':'22', 'N':'23'}

strline = ['']*4
n = 0
for line in sys.stdin:
    strline[n] = line
    n += 1
    if n == 4:
        break

a, b = 0, 0
flag = 0
i = min(len(strline[0]), len(strline[1]))
j = min(len(strline[2]), len(strline[3]))
rlt = []

while(a<i):
    if(strline[0][a] == strline[1][a]):
        if flag == 1 and strline[0][a] in hour.keys():
            rlt.append(strline[0][a])
            break
        if flag == 0 and strline[0][a] in day.keys():
            rlt.append(strline[0][a])
            flag += 1

    a += 1

while(b<j):
    if(strline[2][b] == strline[3][b] and strline[2][b].isalpha()):
        rlt.append(b)
        break
    b += 1

print("%s %s:%02d" % (day[rlt[0]], hour[rlt[1]], rlt[2]))


'''
3485djDkxh4hhGE
2984akDfkkkkggEdsb
s&hgsfdk
d&Hyscvnm
'''