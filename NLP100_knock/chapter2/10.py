# Yukihiro Suzuki 2017/12/20

import pandas as pd

data = pd.read_table("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt", header=None)

print(data.count())
print(len(data))


with open("hightemp.txt", "r") as f:
	print(len(f.readlines()))
####################
