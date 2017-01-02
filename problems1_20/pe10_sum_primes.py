import pe7_10000th_prime as P7
# print P7.isPrime(5)

def sum_prime(upto):
	sum_tem=2
	i=3
	while i<upto:
		if P7.isPrime(i):
			sum_tem+=i
		i+=2

	return sum_tem
print sum_prime(2000000)
# 2000000