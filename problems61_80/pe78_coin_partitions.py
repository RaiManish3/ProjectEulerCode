#############following code takes too long to execute.
# def coin_func_main(number):
# 	lst=[1 for i in xrange(number+1)]

# 	for i in xrange(2,number+1):
# 		for j in xrange(i,number+1):
# 			lst[j]+=lst[j-i]
# 		print i
# 	print lst
# coin_func_main(50000)


############## VERY EFFICIENT
def coin_func_2():
	lst=[]
	lst.append(1)

	n=1
	while 1:
		i=0
		pent=1
		lst.append(0)

		while pent<=n:
			sign=-1 if (i%4>1) else 1
			lst[n]+=sign*lst[n-pent]

			lst[n]%=1000000
			i+=1

			j=(i/2+1) if (i%2==0) else -(i/2+1)
			# generalised pentagonal numbers where j is positve and negative alternatively
			pent=(j*(3*j-1))/2

		if lst[n]==0: return n
		# if n==10:
		# 	return lst
		n+=1
		# print n

print coin_func_2()