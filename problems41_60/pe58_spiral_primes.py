import math
import time
start=time.time()

######################################################################################
# ================================EXECUTION TIME: 3.5s================================

"""
	BRUTE FORCE: GENERATE THE CORNERS, CHECK FOR PRIMALITY AND COUNT THE PRIMES
	COUNT THE NUMBERS, TAKE RATIO AND COMPARE. THAT'S ALL.
"""

def isPrime(a):
	if a%2==0:
		return 0
	stop_f=math.sqrt(a)
	stop=int(stop_f)

	if stop_f==stop:
		return 0

	for i in xrange(3,stop+1,2):
		if a%i==0:
			return 0
	return 1


def spiral_p(below_this):
	num,i=1,1
	d_prime=0
	t_num=1

	while 1:
		inc=2*i
		for x in xrange(4):
			num+=inc
			if isPrime(num):
				d_prime+=1
		t_num+=4
		if float(d_prime)/t_num<below_this:
			return 2*i+1
		i+=1

# print spiral_p(0.1)
# print time.time()-start