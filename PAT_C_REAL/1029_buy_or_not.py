#Author:Yuki
# -*- coding: utf-8 -*-
flag=[]
strpearl=[]
pearlsin = input()
pearls_want = input()
lenwant = len(pearls_want)
lenin = len(pearlsin)
for p in pearlsin:
    strpearl.append(p)
for pearl_want in pearls_want:
    if pearl_want in strpearl:
        flag.append(True)
        strpearl.remove(pearl_want)
    else:
        flag.append(False)
if flag.count(True)==len(pearls_want):
    print("Yes" + " " + str(lenin-lenwant))
else:
    print("No" + " " + str(flag.count(False)))

