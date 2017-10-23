#Author:Yuki
# -*- coding: utf-8 -*-
str_in = input()
num=[int(n) for n in str_in.split()]
A = int(num[0])
B =int(num[1])
Q = int(A//B)
#" / "表示 浮点数除法，返回浮点结果;" // "表示整数除法。
R = A-B*Q
print(Q,R)
