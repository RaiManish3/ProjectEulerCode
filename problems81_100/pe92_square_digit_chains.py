import time
begin=time.time()

##################################################################################################
# ================================EXECUTION TIME:40s=============================================

"""
	CACHING.
	THERE'S MUCH MORE BETTER APPROACH TO THIS PROBLEM.
	NOTE THAT 38,308,3008,30008,... ALL ARRIVE AT THE SAME RESULT;
	SO WE MAY GENERATE ONE SUCH PATTERN; IF THAT PATTERN RESULTS IN 89;
	WE CALCULATE HOW MANY SUCH PATTERNS CAN BE CONSTRUCTED USING COMBINATORICS.
	AND ADD THAT TO COUNT THEN GENERATE A DIFFENRENT PATTERN;

	NUMBER: abcdefg;	a>=b>=c>=d>=e>=f>=g

"""

upto=10000000
lst=[-1 for i in xrange(upto)]
lst[1]=0
lst[89]=1

def main():

	count=1
	for i in xrange(1,upto):
		# skip the already filled cells
		if lst[i]!=-1:
			continue

		number=i
		ll=[]										#store the sequence of numbers leading to 89 or 1
		# print number
		while number!=89 or number!=1:
			ll.append(number)
			n=0
			flag=-1
			while number!=0:
				n+=(number%10)**2
				number/=10
			number=n

			if lst[number]==1:						#if that number showed up before
				flag=1
				break
			if lst[number]==0:					
				flag=0
				break

		if number==89 or flag==1:					#count every element of the list and update the lst
			for i in ll:
				lst[i]=1
			count+=len(ll)

		if number==1 or flag==0:
			for i in ll:
				lst[i]=0		

		del ll[:]
	return count

print main()
print time.time()-begin