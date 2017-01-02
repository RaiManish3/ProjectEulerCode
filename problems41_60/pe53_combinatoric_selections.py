import time
start=time.time()

#####################################################################################
# ===============================EXECUTION TIME:0.6ms================================

"""
	 ELEMENTARY SCHOOL APPROACH:
	 n C r = n*(n-1)*...*(n-r-1)/r*(r-1)...*1
	 SYMMETRY:
	 n C r = n C (n-r)

"""

def com_sel(limit):
	t_count=0
	for n in xrange(23,101):
		for r in xrange(1,n/2+1):
			num_tmp=numerator=n
			r_tmp=denominator=r

			for x in xrange(r-1):
				numerator*=(num_tmp-1)
				denominator*=(r_tmp-1)
				num_tmp-=1
				r_tmp-=1

			if numerator/denominator>limit:
				t_count+=(n-2*r+1)
				break

	return t_count

print com_sel(1000000)
print time.time()-start