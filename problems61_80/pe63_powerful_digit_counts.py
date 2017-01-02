import time
start=time.time()

###################################################################################
# =============================EXECUTION TIME: 4ms=================================

def get_power(a,b):
	num=a

	l1=[]
	while num!=0:
		l1.append(num%10)
		num/=10

	tmp,carry=0,0

	for x in xrange(b-1):
		l=len(l1)
		for j in xrange(l):
			tmp=l1[j]*a
			l1[j]=(tmp+carry)%10
			carry=(tmp+carry)/10
		while carry!=0:
			l1.append(carry%10)
			carry/=10

	return len(l1)


def main():
	digit=2
	count=9
	while 1:
		for i in xrange(4,10):
			l_count=get_power(i,digit)
			if l_count==digit:
				count+=1
			elif i==9:
				return count
		digit+=1

print main()
print time.time()-start