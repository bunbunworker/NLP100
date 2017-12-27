# -*- coding:utf-8 -*-
# Yukihiro Suzuki 2017/12/27
import re
from collections import Counter

with open("col1.txt") as f:
	data = list(row.replace("\ufeff","").strip("\n") for row in f)
	data = list(row.split("\t") for row in data)
	col1 = list(row[0] for row in data)
	print(Counter(col1))
		
