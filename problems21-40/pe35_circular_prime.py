import max_prime_under as mp
import time
start_time=time.time()

lst=[x for x in xrange(1000000)]
lst[2]=-1
count=0

def main(upto):
	global count
	for i in xrange(3,upto,2):

		if lst[i]!=-1:

# ------------------------------------------------------------------------------

			number=i
			l=[]
			while number>0:
				l.append(number%10)
				number/=10

			flag=0

			for x in l:
				if x in [0,2,4,6,8]:
					flag=1
					break 

			if flag==1:
				continue

# -----------------------------------------------------------------------------

# ================================================================================

			if mp.isPrime(i):
				
				digit=len(l)
				l2=[]
				l2.append(i)

													# l=[1,3,5,2]
													# l2=[2531]
													# digit=4

				for x in xrange(digit-1):
					d=digit-1
					j=0
					number2=0
					while d>=0:
						number2+=l[(digit-2-x-j)%digit]*(10**d)
						d-=1
						j+=1

													# print number2
					if mp.isPrime(number2):
						l2.append(number2)

				if len(l2)==digit:
					for x in l2:
						lst[x]=-1
						count+=1


# ===================================================================================

main(1000000)

print count
print time.time()-start_time
