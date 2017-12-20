# -*- coding: utf-8 -*-
# Yukihiro Suzuki 2017/12/18

import re

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

# My Answer.
data = str.split(" ")
keys = []
values = []
r = 1
for i in data:
    if r==1 or r==5 or r==6 or r==7 or r==8 or r==9 or r==15 or r==16 or r==19 :
        Ans = i[0]
    else:
        Ans = i[0:2]
    keys.append(Ans)
    values.append(r)
    r += 1

dic = dict(zip(keys,values))
print(dic)

# Web Answer.
# enumerate の引数の1は、インデックスを1から始めることを意味している。
dic = {word[:2-(i in (1,5,6,7,8,9,15,16,19))]:i for i, word in enumerate(str.replace(".","").split(), 1)}
print(dic)
