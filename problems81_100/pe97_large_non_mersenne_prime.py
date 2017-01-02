def all_of_2(upto):
	upto-=1
	limit=10**10		#last ten digits
	
	# 509 and 24 are divisors of upto-1
	part=upto/(509*24)-1
	number=(2**(509*24))%(limit)
	n=number

	for i in xrange(part):
		number=(number*n)%limit

	return (number*2*28433+1)%limit

print all_of_2(7830457)