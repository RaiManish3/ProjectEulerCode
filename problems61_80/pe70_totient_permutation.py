import max_prime_under as mp
import time
start=time.time()

#######################################################################################
# ========================EXECUTION TIME:1s==========================================

"""
	WE NEED TO GET MINIMAL RATIO n/phi(n) FOR WHICH phi(n) is a permutation of 'n'.
	OBSERVATIONS:
		RATIO= 1/product of (1-1/p)
		RATIO IS MINIMUM WHEN P IS MAX AND PRODUCT CONSISTS OF MINIMAL NUMBER OF TERMS.

	NOTE THAT PRIME NUMBER CAN NEVER PROVIDE SUCH A PERMUTATION
	SO I FIRST WENT FOR THE nth power OF EACH PRIME ; BUT THERE WEREN'T ANY SUCH
	PERMUTATION. (THIS IS THE FUNCTION main2())

	THEN THERE IS OPTION FOR PRODUCT OF TWO PRIMES IN POWER ONE OR HIGHER.
	I FIRST WENT FOR THE POWER 1. (CODE FOR THAT IS main())

	FORTUNATELY I GOT A SOLUTION THERE.
	NOTE THAT CONSIDERING HIGHER POWER DOES NOT CHANGE THE RATIO AS WAS IN ANY OTHER POWER
	>=1

	THE RANGE: P SHOULD BE MAX, SO CREATED A MUCH LARGER PRIME_LIST AND STARTED FROM
	HIGHER END.

"""

prime_list=[]

def gen_prime_list(upto):
	for i in xrange(1001,upto-1,2):
		if mp.isPrime(i):
			prime_list.insert(0,i)

# def main2(upto):
# 	gen_prime_list(upto)

# 	for i in prime_list:
# 		power=2
# 		while 1:
# 			num=i**power
# 			if num>10000000:
# 				break
# 			str1=str(num)
# 			str2=str(num-num/i)

# 			str3=''.join(sorted(str1))			
# 			str4=''.join(sorted(str2))			
# 			print i,power,num,str3,str4

# 			if str3==str4:
# 				return num,str1,str2
# 			power+=1

def main(upto):
	gen_prime_list(upto)
	l=len(prime_list)
	min_ratio=10
	num=''

	for i in xrange(l):
		for j in xrange(i+1,l):
			n=prime_list[i]*prime_list[j]
			str1=str(n)
			if n>10000000:
				continue
			str2=str((prime_list[i]-1)*(prime_list[j]-1))

			ratio=float(n)/((prime_list[i]-1)*(prime_list[j]-1))

			str3=''.join(sorted(str1))
			str4=''.join(sorted(str2))

			if str3==str4 and ratio<min_ratio:
				min_ratio=ratio
				num=str1
	return num,min_ratio
				


# print main(8000)
# print time.time()-start
# print prime_list
# ==================================================================================
# str1="5314"
# str2=''.join(sorted(str1))
# print str2