# -*- coding: UTF-8 -*-

#约定俗成的写法plt
import matplotlib.pyplot as plt

curV = 100
curV_p1 = 100
curV_p2 = 100
stanV = 100
p = 0.7
i = 0.2
d = 0.1
index = 0
x = []
v = []
s = []
dd = []
sd = []
while index < 200:
    x.append(index)
    index = index + 1
    v_d = (curV - stanV) * p + (curV_p1 - stanV) * i + (curV_p2 - stanV) * d
    dd.append(v_d)
    sd.append(0)
    curV_p1 = curV
    curV_p2 = curV_p1
    curV = curV - v_d
    print (index,v_d,curV)
    v.append(curV)
    s.append(stanV)
    if index == 50:
        stanV = 50
    elif index == 150:
        stanV = 200

plt.plot(x,dd)
plt.plot(x,sd)
plt.show()