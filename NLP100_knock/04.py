# -*- coding: utf-8 -*-
# Yukihiro Suzuki 2017/12/18

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# My Answer.
data = str.split(" ")
keys = []
values = []
r = 1
for i in data:
    if r==1 or r==5 or r==6 or r==7 or r==8 or r==9 or r==15 or r==16 or r==19 :
        print(r)
        Ans = i[0]
    else:
        Ans = i[0:2]
    keys.append(Ans)
    values.append(r)
    r += 1

dic = dict(zip(keys,values))
print(dic)
# Web Answer.

