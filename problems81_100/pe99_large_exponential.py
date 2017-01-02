import math

f=open('p099_base_exp.txt','r')
min_num=(1,1,0)
count=1

for lines in f.readlines():
	base,exp=lines.split(',')
	base=int(base)
	exp=int(exp)
	if exp*math.log10(base)>min_num[1]*math.log10(min_num[0]):
		min_num=(base,exp,count)
	count+=1

print min_num