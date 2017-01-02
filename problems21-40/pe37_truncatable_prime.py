import max_prime_under as mp
import time
start=time.time()

# ##################################################################################
# =========================Execution time: 1.5s=====================================

count=0
t_sum=0
limit=1000000
# -------------------------limit is rather vague, i ran it on a trial basis
# --------------------------and the count makes itself 11 within that range

for i in xrange(11,limit):

# -------------------------------------------------Limiting the cases
	if i%10==9:
		continue
	str1=str(i)
	if str1[0] in ['1','4','6','8','9']:
		continue

# --------------------------------------------------

	if mp.isPrime(i):
		number=i
		digits=0

		while number!=0:
			digits+=1
			number/=10

		d=digits-1
		number1=i
		number2=i


		while d>0:
			number1%=(10**d)
			number2/=10
			# print i,number1,number2
			if not mp.isPrime(number1):
				break
			if not mp.isPrime(number2):
				break
			d-=1

		if d==0:
			count+=1
			t_sum+=i
			# print i,"================="

		if count==11:
			break


# ===================================================================================


print t_sum
print count
print time.time()-start
