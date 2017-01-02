import max_prime_under as mp
import time
start=time.time()

######################################################################################
# ================================EXECUTION TIME:108s================================

"""
	HEAVILY BRUTE FORCED;
	WITHIN MY KNOWLEDGE DOMAIN, I TRIED TO IMPROVE THE RUNTIME BUT ALL IN VAIN.

	METHOD: 
	SAME AS THE QUESTION SAYS- TAKE A TWO PRIME, SEE IF THERE CONCATE IS ALSO PRIME
	THEN TAKE THREE PRIME, DO THE SAME.. TAKE FIVE AND IF THEY SATISFY THE CONDITION
	UPDATE TOTAL_SUM.

	SLIGHT IMPROVEMENT OF BREAKING LOOP IS HARNESSABLE IF WE KEEP LOOP ITERATION VARIABLES
	IN INCREASING ORDER.
"""

def check_conditions(i,j):
	if mp.isPrime(int(str(i)+str(j))) and mp.isPrime(int(str(j)+str(i))):
		return 1
	return 0


def min_prime_set(sum_limit):
	t_sum=sum_limit
	p_sum=0
	lst=[]

	for i in xrange(3,10000,2):
		p_sum=i
		if p_sum>=t_sum/5:
			break
		if mp.isPrime(i):
			for j in xrange(i+2,10000,2):
				p_sum=i+j
				if p_sum>=t_sum/4:
					break
				if mp.isPrime(j):
					if check_conditions(i,j):
						for k in xrange(j+2,10000,2):
							p_sum=i+j+k
							if p_sum>=t_sum/3:
								break
							if mp.isPrime(k):
								if check_conditions(i,k) and check_conditions(j,k):
									for l in xrange(k+2,10000,2):
										p_sum=i+j+k+l
										if p_sum>=t_sum/2:
											break
										if mp.isPrime(l):
											if check_conditions(i,l) and check_conditions(j,l) and check_conditions(k,l) :	
												for m in xrange(l+2,10000,2):
													p_sum=i+j+k+l+m
													if p_sum>=t_sum:
														break
													if mp.isPrime(m):
														if check_conditions(i,m) and check_conditions(j,m) and check_conditions(k,m) and check_conditions(l,m):
															# print p_sum
															t_sum=p_sum
															lst=[i,j,k,l,m]


	return t_sum,lst	

	

print min_prime_set(10000000)
print time.time()-start