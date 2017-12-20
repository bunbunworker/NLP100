# -*- coding: utf-8 -*-
# Yukihiro Suzuki 2017/12/20

# My Answer
def cipher(s):
	return ("".join(chr(219-ord(c)) if c.islower() else c for c in s))

s = "I am NLPer, isn't you?"

print(cipher(s))
print(cipher(cipher(s)))
	
