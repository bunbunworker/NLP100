# -*- coding: utf-8 -*-
# Yukihiro Suzuki 2017/12/19

# My Answer
def n_gram_words(n,data):
	i=0
	result=[]
	s = data.split(" ")
	for i in range(len(s)-(n-1)):
		result.append(s[i:i+n])
		i+=1
	return result

def n_gram_chars(n,data):
	return {tuple(data[i:i+n]) for i in range(len(data)-(n-1))}

sentence = "I am an NLPer"

Ans1 = n_gram_words(2,sentence)
Ans2 = n_gram_chars(2,sentence)
print(Ans1)
print(Ans2)

# Web Answer
def n_gram(s, n): return {tuple(s[i:i+n]) for i in range(len(s)-n+1)}

s = "I am an NLPer"
print(n_gram(s,2))
print(n_gram([t.strip(".,") for t in s.split()], 2))	
