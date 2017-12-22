# -*- coding; utf-8 -*-
# Yukihiro Suzuki 2017/12/20

# My Answer
import random

s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

data = s.strip(",.")
data = data.split(" ")
print(data)
result = []
words = []

# main loop
for t in data:
	if len(t)>4:
		words = ("".join(sorted(t[1:-1], key=lambda k: random.choice(k))))
		#print(words)
		words = t[0] + words + t[-1]
	else:
		words = t
	result.append(words)

print(result)			


# Web Answer
# typo  = lambda s: " ".join(t[0]+"".join(sorted(t[1:-1], key=lambda k:random()))+t[-1] if len(t) > 4 else t for t in s.split())

# s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
# print(typo(s))

# Please use this method.
print(random.sample("abcd",4))

