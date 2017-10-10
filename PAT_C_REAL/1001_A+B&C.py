#Author:Yuki
T=input()
T=int(T)
t=0
flag=[]
while t<=T-1:
    str_in = input()
    num=[int(n) for n in str_in.split()]
    num = num[:3]
    if num[0]+ num[1] > num[2]:
        flag.append(True)
    else:
        flag.append(False)
    t += 1
for t_ in range(1,T+1):
    print('Case #' + str(t_) + ": " + str(flag[t_-1]).lower())


