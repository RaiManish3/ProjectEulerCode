import pe33_digit_cancelling_fractions as dcf
import time
begin=time.time()

##################################################################################
# ===========================EXECUTION TIME:44s===================================

"""
	I HAVE IMPLEMENTED A NARROWED BRUTE FORCE.
	CAN BE IMPROVED USING Stern-Brocot tree AND STACK
"""

def count_frac(upto):
	t_count=0
	for d in xrange(5,upto+1):
		start=d/3+1
		stop=d/2+1
		for n in xrange(start,stop):
			ratio=float(n)/d
			if ratio>1/3.0 and ratio<1/2.0:
				if dcf.gcd(n,d)==1:
					t_count+=1

		# print d,t_count

	return t_count

# print count_frac(12000)
# print time.time()-begin
