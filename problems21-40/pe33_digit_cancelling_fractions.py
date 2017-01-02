import time
start_time=time.time()

######################################################################################
# ===================================EXECUTION TIME: 2ms================================

def gcd(a,b):
	if a==0:
		return b
	return gcd(b%a,a)


def cancel_fraction():
	lst=[]
	for i in xrange(10,100):
		ones1=i%10
		tens1=i/10
		if ones1==0:
			continue
		for j in xrange(i+1,100):
			ones2=j%10
			tens2=j/10
			if ones2==0:
				continue

			if ones2==ones1:
				if float(tens1)/tens2==float(i)/j:
					lst.append([i,j])

			if ones2==tens1:
				if float(ones1)/tens2==float(i)/j:
					lst.append([i,j])

			if tens2==ones1:
				if float(tens1)/ones2==float(i)/j:
					lst.append([i,j])

  			if tens2==tens1:
				if float(ones1)/ones2==float(i)/j:
					lst.append([i,j])


	# return lst
	denominator,numerator=1,1
	for x in xrange(len(lst)):
		common=gcd(lst[x][0],lst[x][1])
		numerator*=lst[x][0]/common
		denominator*=lst[x][1]/common

	return denominator/gcd(numerator,denominator)



# print cancel_fraction()
# print time.time()-start_time