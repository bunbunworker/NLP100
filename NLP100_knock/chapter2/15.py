# -*- coding: utf-8 -*-
# Yukihiro Suzuki 2017/12/20

import re
import sys

# My Answer
with open("hightemp.txt", "r") as f:
	data = list(row.replace("\ufeff","").strip("\n") for row in f)
	data = list(row.split("\t") for row in data)

print(data[int(input("input num:")):])

# Web Answer
with open("hightemp.txt") as f:
	print("".join(f.readlines()[-int(sys.argv[1]):]))
