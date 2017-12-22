# -*- coding: utf-8 -*-

str1 = "パトカー"
str2 = "タクシー"
Ans = ""

for i in range(0,4):
    str = (str1 + str2)[i::4]
    Ans += str

print(Ans)

# Please use zip(for) because the above program doesn't work when these sentence's size are different.
