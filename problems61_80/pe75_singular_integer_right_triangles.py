import math
import pe33_digit_cancelling_fractions as dcf
import time
begin=time.time()

# ################################################################################
# =======================EXECUTION TIME: 3s======================================

"""
	REFER TO WIKIPEDIA PAGE: https://en.wikipedia.org/wiki/Pythagorean_triple
"""

lst=[0 for i in xrange(1500001)]

def pythagorean_triplet(upto):
	t_count=0
	m_limit=int(math.sqrt(upto))

	for m in xrange(2,m_limit):
		for n in xrange(1,m):
			if (m+n)%2==1 and dcf.gcd(n,m)==1:
				a=m*m-n*n
				b=2*m*n
				c=m*m+n*n
				p=a+b+c
				while p<=upto:
					lst[p]+=1
					if lst[p]==1: t_count+=1
					if lst[p]==2: t_count-=1
					p+=(a+b+c)
	return t_count

print pythagorean_triplet(1500000)
print time.time()-begin