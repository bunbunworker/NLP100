# -*- coding: utf-8 -*-
# Yukihiro Suzuki 2017/12/27
import sys,math

data = [line for line in open("hightemp.txt","r")]
print(data)
unit=math.ceil(len(data)/int(sys.argv[1]))

for i in range(int(sys.argv[1])):
	with open("file"+str(i+1)+".txt","w") as f:
		f.write("".join(data[i*unit:(i+1)*unit]))

