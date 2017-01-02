import time
start_time=time.time()
import max_prime_under as mp

# ======================================Execution time: 1.2s==========================

"""
	AS N=0 IS ALLOWED. EQUATION CORRESPONDING TO IT YIELDS TMP=B IMPLYING THAT B IS A PRIME
	NUMBER. THERE WE CUT SEVERAL ITERATIONS. FURTHERMORE IT ALSO APPLIES 'B' CANNOT BE NEGATIVE
	SO WE CHECK FOR POSITIVE VALUES ONLY.

	TWO MORE DEDUCTION CAN BE MADE THAT 
	IF B=EVEN, THEN FOR N=2 WE HAVE 4+2A+B, AS B IS EVEN SO THE SUM IS EVEN => NOT PRIME.
	IF A=EVEN, THEN FOR N=3 WE HAVE 9+3A+B, FROM ABOVE B IS ODD SO 9+B IS EVEN 
	AND SO IS '3A' BUT THEN OVERALL SUM IS NOT PRIME.

"""

######################################################################################

def quad_prime(lim1,lim2):
	max_primes=0
	a_max,b_max=0,0
	for a in xrange(-lim1+1,lim1,2):
		for b in xrange(3,lim2,2):       
			if not mp.isPrime(b):
				continue
			n=1
			while 1:
				tmp=n**2+a*n+b
				if tmp<0:
					break
				if not mp.isPrime(tmp):
					break
				n+=1
			if n>max_primes:
				max_primes=n
				a_max,b_max=a,b

	return a_max,b_max,a_max*b_max,max_primes+1


print quad_prime(1000,1000)
print time.time()-start_time

######################################################################################