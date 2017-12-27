# -*- coding:utf-8 -*-
# Yukihiro Suzuki 2017/12/27

with open("hightemp.txt") as f:
	print(set([line.split("\t")[0] for line in f]))

