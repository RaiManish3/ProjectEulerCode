import pe33_digit_cancelling_fractions as dcf
import time
start=time.time()

######################################################################################
# =============================EXECUTION TIME:4s=====================================

"""
	WE CAN NARROW DOWN RANGE FOR SEARCH BY OBSERVING FEW THINGS.
	OBSERVATIONS:
	NUMBERATOR CANNOT BE MORE THAN 428572 AS THE DENOMINATOR CAN MAX GO TO 2000000
	AND FOR CLOSER VALUE WE NEED GEATER DENOMINATOR.
"""

frac_list=[]

def gen_fractions():
	reference1=0.4
	reference2=float(3)/7
	lst=[2,5]

	for n in xrange(428500,428572):
		for d in xrange(int(1/reference2*n),int(2.5*n)):
			if float(n)/d<reference2 and float(n)/d>=reference1:
				if dcf.gcd(n,d)==1:
					reference1=float(n)/d
					lst[0],lst[1]=n,d

	return lst

# print gen_fractions()
# print time.time()-start