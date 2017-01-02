

def isPal(n_str):

	l=len(n_str)
	i,j=0,l-1
	while i<j:
		if n_str[i]!=n_str[j]:
			break
		i+=1
		j-=1
	if i<j:
		return 0
	else :
		return 1

sum_all=0

def main(upto):
	global sum_all
	for i in xrange(1,upto):
		if isPal(str(i)):
			number=i
			lst=[]

			while number>0:
				lst.append(number%2)
				number/=2

			str1=''.join(map(str,lst))
			if isPal(str1):
				sum_all+=i
				# print i, str1

# main(1000000)
# print sum_all