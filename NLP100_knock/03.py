# -*- coding: utf-8 -*-

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# My Answer.
data = str.split(" ")
print(data)
result = []

for i in data:
    Ans = len(i.strip(",."))
    result.append(Ans)

print(result)

# Web Answer.
count = [len(i.strip(",.")) for i in str.split()]
print(count)
