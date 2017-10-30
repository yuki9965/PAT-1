#Author:Yuki
# -*- coding: utf-8 -*-
#2017/10/12
coes = input()
coe = [int(i) for i in coes.split()]
N = coe[0]
P = coe[1]
str_in = input()
num = [int(t) for t in str_in.split()]
num = num[:N]
num_max = num[:]
if max(num)<=min(num)*P:
    print(len(num))
while max(num_max)>min(num_max)*P:
    num_max.remove(max(num_max))
while max(num)>min(num)*P:
    num.remove(min(num))
if len(num_max)<len(num):
    print(len(num))
else:
    print(len(num_max))