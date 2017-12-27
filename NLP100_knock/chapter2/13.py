# -*- coding* utf-8 -*-
# Yukihiro Suzuki 2017/12/27

f1 = open("col1.txt","r")
f2 = open("col2.txt","r")

with open("col1.txt","r") as f1, open("col2.txt","r") as f2, open("13.txt","w") as f3:
	f3.write("".join([row1.strip("\n")+"\t"+row2 for row1,row2 in zip (f1,f2)]))
	
