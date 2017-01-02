# can be made efficient by caching the length of existing sequence.
#basically DP.

def collatz(start):
	max_count=1
	while start<1000000:
		# print "start= ",start
		count=1
		tem_start=start
		while tem_start!=1:
			if tem_start%2==0:
				tem_start/=2
			else:
				tem_start=3*tem_start+1
			count+=1
		if count>max_count:
			max_count=count
			number=start
		start+=2
		# print "max_count= ",max_count 

	return number


print collatz(10001)