import math
import time
start=time.time()

######################################################################################
# ===============================EXECUTION TIME: 4ms===================================

f=open('words.txt','r')
str1=f.read()
lst=list(str1.split(','))
# print lst

count=0
letter_dic={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def main():
	global count
	for i in lst:
		p_sum=0
		l=len(i)
		for j in xrange(l):
			p_sum+=letter_dic[i[j]]

		num=(-1+math.sqrt(1+8*p_sum))/2

		if num==int(num):
			count+=1
			# print i,p_sum

main()
# print count
# print time.time()-start