# -*- coding:utf-8 -*-
# Yukihiro Suzuki 2017/12/27

with open("hightemp.txt") as f:
	data = (row.split("\t")[2] for row in f)
	print(sorted(data))
