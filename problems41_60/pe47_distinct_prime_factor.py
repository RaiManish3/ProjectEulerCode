import max_prime_under as mp
import time
start=time.time()

#######################################################################################
# ==============================EXECUTION TIME: 8s=======================================

"""
	Tried many ways for the optimisation;
	1. simple brute force; Run a loop over all divisors upto i/2+1 and check if they are prime.
	takes much much longer time , not at all diserable I would say.
	2.Use DP to store the already processed primes.
	3.Generate the prime_list itself upto 1415 (My guess was that within 2million i would get such a number.)

	The lower limit: I kept it to be 210=2*3*5*7
	this is so because to choose minimum number I will have to choose 4 lowest distinct primes
	2,3,5,7..

"""

prime_list=[]
prime_list.append(2)

def gen_prime_list():
	for i in xrange(3,1415,2):
		if mp.isPrime(i):
			prime_list.append(i)


def main(num_distinct):
	lst=[0 for i in range(num_distinct)]
	gen_prime_list()
	i=210

	while 1:

		count=0
		
		for j in prime_list:
			if j*2>i:
				break
			if i%j==0:
				count+=1

		lst[0:num_distinct-1]=lst[1:num_distinct]
		if count==num_distinct:
			lst[num_distinct-1]=1
		else :
			lst[num_distinct-1]=0

		if not 0 in lst:
			return i-num_distinct+1

		# print i, lst
		i+=1

print main(4)
print time.time()-start
