import time
import math
import max_prime_under as mp

N=600851475143
start_time=time.time()

start=int(math.sqrt(N))
if start%2==0:
	start-=1

max_p=1

for i in xrange(start,3,-2):
	if N%i==0:
		if mp.isPrime(i):
			max_p=i
			break



print max_p
print time.time()-start_time