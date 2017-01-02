import time
begin=time.time()
####################################################################################
# ==============================EXECUTION TIME:88s==================================

"""
	BRUTE FORCE WITH CACHING.
"""

lst=[0 for i in xrange(69,1000001)]

fact_dic={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

def digit_factorial(upto):
	target=60
	t_count=0
	for number in xrange(69,upto+1):
		l1=[]
		l1.append(number)
		n=number
		if lst[number-69]==0:
			while 1:
				fact_sum=0
				while n>0:
					fact_sum+=fact_dic[n%10]
					n/=10
				if fact_sum in l1:
					ind=l1.index(fact_sum)
					for i in xrange(ind+1):
						if l1[i]<upto:
							lst[l1[i]-69]=len(l1)-i
					break
				n=fact_sum
				l1.append(n)

		if lst[number-69]==60:
			t_count+=1
		# print number,lst[number-69]

	return t_count

print digit_factorial(1000000)
print time.time()-begin			
