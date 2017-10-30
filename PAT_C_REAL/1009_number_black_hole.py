#Author:Yuki
# -*- coding: utf-8 -*-
#2017/10/24
res=0
N = input()
if int(N) == 0:
    print("0000" + " - " + "0000" + " = 0000")
elif N[1]==N[0]==N[2]==N[3]:
    print(str(N) + " - "+ str(N) + " = 0000")

else:
    while N!=6174:
        Nfall = ''.join(sorted(str(N), reverse=True))
        Nrise = ''.join(sorted(str(N), reverse=False))
        N = int(Nfall) - int(Nrise)
        print(Nfall + " - " + Nrise + " = " + str(N))
