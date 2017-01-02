import max_prime_under as mp
import time
start=time.time()

##############################################################################
# ===========================================================================

"""
	FOLLOWING INCLUDES THE LATER CODES:
	ONE THAT USES FORMULA : n/phi(n)= product of ditinct prime factors/product of (ditinct prime factors-1)
	IT IS RATHER SLOW.

	SECOND ONE IS MORE LOGICAL :
	FORMULA SAME AS ABOVE EXCEPT ONE CHANGE : n/phi(n)= 1/product of (1-1/P) ; where P is prime.
	so in order to obtain high value for LHS we should take into account the smallest P's available
	so we take the product of samllest P till the product < limit.
"""

# ----------------------------------------------------------------------------------


def gen_prime_list(upto):
	result=2
	for i in xrange(3,upto-1,2):
		if mp.isPrime(i):
			result*=i
		if result>upto:
			return result/i


# print gen_prime_list(1000000)
# -----------------------------------------------------------------------------------