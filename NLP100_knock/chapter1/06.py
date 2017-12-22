# -*- coding* utf-8 -*-

# My Answer
def n_gram_chars(n,data):                                  
	return {tuple(data[i:i+n]) for i in range(len(data)-n+1)}

s1 = "paraparaparadise"
s2 = "paragraph"

X = set(n_gram_chars(2,s1))
Y = set(n_gram_chars(2,s2))

print("union")
print(X|Y) # Union set
print("intersention")
print(X&Y) # Intersention set
print("difference")
print(X-Y) # Difference set

if n_gram_chars(2,"se") <= X: print("X is OK!")
if n_gram_chars(2,"se") <= Y: print("Y is OK!")

# Maybe, the below method is better.
print("se" in {"a","se"})

