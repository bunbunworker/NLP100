# -*- coding: utf-8 -*-
# Yukihiro Suzuki 2017/12/23

with open("hightemp.txt","r") as f1, open("col1.txt","w") as f2, open("col2.txt","w") as f3:
	data = list(row.replace("\ufeff","").strip("\n") for row in f1)
	data = list(row.split("\t") for row in data)
	f2.write("\n".join(row[0] for row in data))
	f3.write("\n".join(row[1] for row in data))
	data1 = list(row[0] for row in data)
	data2 = list(row[1] for row in data)
print(data1)
print(data2)
