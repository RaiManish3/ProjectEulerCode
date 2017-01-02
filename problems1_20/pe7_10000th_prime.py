import math
import time
begin = time.time()

# http://stackoverflow.com/questions/26791129/find-10000th-prime-number
# Basic idea for time reduction  is that
# In isPrime fn you iterate from i=3 to the sqrt of 'a'
# further in findme fn as all primes other than  2 are odd hence start i from 3 and 
# increment by 2

def isPrime(a):
	stop= int (math.sqrt(a))
	for i in xrange(3,stop+1,2):
		if a%i==0:
			return 0
	return 1


def findme(lim):
	i,counter=3,1

	while 1:
		if isPrime(i):
			counter+=1
		if counter==lim:
			return i
		i+=2


# print findme(10001)
# print time.time()-begin