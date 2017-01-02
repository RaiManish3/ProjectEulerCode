import math
import max_prime_under as mp
import time
start=time.time()

###############################################################################
# ==============================EXECUTION TIME: 0.03s===========================

def main():
	n=13
	while 1:
		count=0
		if mp.isPrime(n):
			n+=2
			continue
		stop=int(math.sqrt((n-1)/2))
		for i in xrange(1,stop+1):
			if mp.isPrime(n-2*(i**2)):
				break

			# knoeledge : keeping the i==stop+1 outside does not yield the result.
			if i==stop:
				print n
				print stop
				return

		n+=2

main()
print time.time()-start