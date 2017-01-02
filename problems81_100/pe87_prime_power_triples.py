import max_prime_under as mp
import time
begin=time.time()

########################################################################
# ==========================EXECUTION TIME: 3.4s==========================

prime_lst=[]
prime_lst.append(2)
index_1,index_2=0,0

for i in xrange(3,7072,2):
	if mp.isPrime(i):
		prime_lst.append(i)
		if i<84:
			num_1=i
		if i<369:
			num_2=i

number_lst=[]
l=len(prime_lst)

index_1=prime_lst.index(num_1)
index_2=prime_lst.index(num_2)

# print index_1,index_2
target=50000000

for i in xrange(index_1+1):
	for j in xrange(index_2+1):
		if prime_lst[i]**4+prime_lst[j]**3>target:break
		for k in xrange(l):
			number=prime_lst[k]**2+prime_lst[j]**3+prime_lst[i]**4
			if number>target: break
			number_lst.append(number)


# print len(set(number_lst))
# print time.time()-begin

