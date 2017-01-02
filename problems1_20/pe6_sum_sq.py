# use formula of sum of first natural numbers and sum of squares of the same

def sum_sq_dif(n):
	sum1=((n*(n+1))/2)**2
	sum2=(n*(n+1)*(2*n+1))/6
	return sum1-sum2

print sum_sq_dif(100)