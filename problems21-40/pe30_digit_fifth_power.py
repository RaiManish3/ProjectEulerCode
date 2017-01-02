###################################################################################
# =============================EXECUTION TIME : 0.5 s==============================

# BRUTE FORCE----------------------------------------------------------------------


import time
start_time=time.time()

def main(upto,power):
	t_sum=0
	for i in xrange(11,upto):
		p_sum=0
		number=i
		while number!=0:
			p_sum+=(number%10)**power
			number/=10
		if p_sum==i:
			t_sum+=p_sum

	return t_sum


print main(355000,5)         #BY OBSERVATION WE CAN GET SUCH NUMBERS ONLY UPTO 6 DIGIT NUMBERS. THEIR SUM_LIMIT = 6*9^5= 355000
print time.time()-start_time
