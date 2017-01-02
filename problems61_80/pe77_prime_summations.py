import max_prime_under as mp
import time
begin=time.time()

##############################################################################
# ========================EXECUTION TIME:6ms==================================

def prime_sum(upto,limit):
	prime_lst=[]
	prime_lst.append(2)

	for i in xrange(3,upto,2):
		if mp.isPrime(i):
			prime_lst.append(i)

	l=len(prime_lst)
	target=2

	while 1:
		number_lst=[0 for i in xrange(target+1)]
		number_lst[0]=1

		for i in xrange(0,l):
			for j in xrange(prime_lst[i],target+1):
				number_lst[j]+=number_lst[j-prime_lst[i]]
			if i>target:break
			# if target==12:
			# 	print prime_lst[i],number_lst

		if number_lst[target]>5000:	return target
		target+=1
		del number_lst

print prime_sum(100,12)
print time.time()-begin
